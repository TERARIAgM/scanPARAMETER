import requests
from bs4 import BeautifulSoup
import urllib.parse
from colorama import init, Fore, Style

init(autoreset=True)

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
print(Fore.GREEN + ascii_art)
print(Fore.GREEN + Style.BRIGHT + "══════════════════════════════════════════")
print(Fore.YELLOW + " ⚡ Author  : " + Fore.GREEN + "hbwterminator")
print(Fore.YELLOW + " 🔗 GitHub  : " + Fore.GREEN + "https://github.com/TERARIAgM")
print(Fore.GREEN + Style.BRIGHT + "══════════════════════════════════════════")
def print_log(message, color=Fore.GREEN):
    print(f"{color}[+] {Style.BRIGHT}{message}")

def find_url_parameters(url):
    """Mencari parameter di URL"""
    print_log("Mengecek URL untuk parameter...", Fore.YELLOW)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print_log(f"\n{Fore.CYAN}URL berhasil diakses: {url}\n", Fore.CYAN)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            parameters = []
            for link in links:
                href = link['href']
                parsed_url = urllib.parse.urlparse(href)
                query_params = urllib.parse.parse_qs(parsed_url.query)

                if query_params:
                    parameters.append(query_params)

            if parameters:
                print_log("\n[!] Parameter yang ditemukan:", Fore.GREEN)
                for param in parameters:
                    print(f"{Fore.YELLOW}[*] {param}")
            else:
                print_log("Tidak ada parameter ditemukan di halaman ini.", Fore.RED)
        else:
            print_log(f"Gagal mengakses URL: {url}. Status Code: {response.status_code}", Fore.RED)

    except requests.RequestException as e:
        print_log(f"Error: {e}", Fore.RED)

def grep_links_and_resources(url):
    """Mencari semua link dan resource di halaman"""
    print_log("Mengekstrak semua link dan resource dari halaman...", Fore.YELLOW)
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            print_log("\n[!] Link dan Resource yang ditemukan:", Fore.GREEN)
            
            for tag in soup.find_all(['a', 'link', 'script', 'img']):
                if tag.name == 'a' and tag.get('href'):
                    print(f"{Fore.CYAN}[Link] {tag['href']}")
                elif tag.name == 'link' and tag.get('href'):
                    print(f"{Fore.BLUE}[CSS] {tag['href']}")
                elif tag.name == 'script' and tag.get('src'):
                    print(f"{Fore.YELLOW}[JS] {tag['src']}")
                elif tag.name == 'img' and tag.get('src'):
                    print(f"{Fore.MAGENTA}[IMG] {tag['src']}")
        else:
            print_log(f"Gagal mengakses URL: {url}. Status Code: {response.status_code}", Fore.RED)
    
    except requests.RequestException as e:
        print_log(f"Error: {e}", Fore.RED)

print(f"\n{Fore.MAGENTA}Pilih mode scan:")
print(f"{Fore.YELLOW}1. Scan Parameter URL")
print(f"{Fore.YELLOW}2. Scan Link & Resource (Grep Mode) + Extrak")
mode = input(f"{Fore.CYAN}Pilih Cuy (1/2): {Fore.YELLOW}")

url = input(f"\n{Fore.MAGENTA}Masukkan URL targetnya: {Fore.YELLOW}")

if mode == "1":
    find_url_parameters(url)
elif mode == "2":
    grep_links_and_resources(url)
else:
    print_log("Pilihan tidak valid!", Fore.RED)
