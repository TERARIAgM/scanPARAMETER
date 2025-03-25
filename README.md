## 🔍scanPARAMETER 
# adalah alat berbasis Python yang dirancang untuk membantu pentester dan bug hunter dalam mendeteksi parameter URL, mengekstrak link dan resource, menguji SQL Injection, serta mencari halaman admin pada sebuah situs web.

## ⚒️Fitur 

✅ Scan Parameter URL – Menemukan parameter yang tersembunyi dalam URL untuk eksploitasi lebih lanjut.
✅ Ekstraksi Link & Resource – Mengambil semua link, CSS, JavaScript, dan gambar yang ada di halaman target.
✅ Uji SQL Injection – Menganalisis parameter dalam URL untuk mendeteksi potensi kerentanan SQL Injection.
✅ Pencarian Halaman Admin – Mencari halaman admin menggunakan wordlist yang dapat disesuaikan.
✅ Antarmuka CLI yang Menarik – Menggunakan Rich dan Colorama untuk tampilan yang lebih interaktif.

---

## 🔧Instalasi 

Sebelum menjalankan scanPARAM, jalankan perintah berikut untuk menginstal semua dependensi yang diperlukan

---pip install -r requirements.txt

## 📌 Contoh Hasil Scan

### Scan Link & Resource

| Jenis        | URL                                       |
|-------------|-------------------------------------------|
| 🔗 Link      | https://target.com/page.php?id=123       |
| 🖼️ Gambar    | https://target.com/media/logo.png       |
| 📜 JavaScript | https://target.com/assets/script.js     |
| 🎨 CSS       | https://target.com/style.css            |

**Total link dan resource ditemukan:** `4`

### Scan Parameter URL

| Parameter   | Urlnya Cuyy                                |
|------------|-------------------------------------------|
| id         | https://target.com/page.php?id=123       |
| search     | https://target.com/search.php?query=test |

**Total parameter ditemukan:** `2`

---


💡 Author: hbwterminator

🔗 GitHub: TERARIAgM

---



**scanPARAM by hbwterminator🔍**
