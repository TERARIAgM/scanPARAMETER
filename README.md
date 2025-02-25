scanPARAMETER

🛡️ scanPARAMETER adalah alat berbasis Python untuk mencari parameter di URL dan mengekstrak semua link serta resource dari sebuah halaman web. Cocok digunakan untuk pentesting dan eksplorasi keamanan web.
---

📌 Fitur

✅ Mengecek parameter di dalam URL
✅ Mengekstrak semua link dan resource (CSS, JS, IMG) dari sebuah halaman web
✅ Tampilan terminal yang berwarna menggunakan colorama
✅ Mudah digunakan, hanya dengan memasukkan URL target


---

⚡ Instalasi

Pastikan kamu sudah menginstall Python 3.x di sistem kamu. Kemudian install dependensinya dengan:

pip install requests beautifulsoup4 colorama

Lalu, clone repository ini:

git clone https://github.com/TERARIAgM/scanPARAMETER.git
cd scanPARAMETER


---

🚀 Cara Penggunaan

Jalankan script dengan perintah:

python scanPARAM.py

Kemudian pilih mode scan:
1️⃣ Scan Parameter URL
2️⃣ Scan Link & Resource (Grep Mode)

Masukkan URL target, lalu hasilnya akan ditampilkan di terminal.


---

🖥️ Contoh Output

══════════════════════════════════════════
 ⚡ Author  : hbwterminator
 🔗 GitHub  : https://github.com/TERARIAgM
══════════════════════════════════════════

Pilih mode scan:
1. Scan Parameter URL
2. Scan Link & Resource (Grep Mode) + Extrak

Pilih Cuy (1/2): 1

Masukkan URL targetnya: https://example.com

[+] Mengecek URL untuk parameter...
[+] URL berhasil diakses: https://example.com
[!] Parameter yang ditemukan:
[*] {'id': ['123'], 'page': ['home']}


---

📜 Lisensi

Proyek ini dirilis di bawah lisensi MIT, sehingga bebas digunakan dan dikembangkan lebih lanjut.


---

👤 Author

hbwterminator
🔗 GitHub: TERARIAgM


---
