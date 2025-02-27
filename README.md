## 🔍scanPARAM 

scanPARAM adalah alat untuk mencari parameter URL dan mengekstrak semua link serta sumber daya (CSS, JavaScript, Gambar) dari sebuah halaman web.

## ⚒️Fitur 

✅ Scan Parameter URL – Mendeteksi parameter dalam URL dan menampilkannya secara rapi.

✅ Grep Link & Resource – Mengekstrak semua link dan sumber daya dari halaman web dengan format yang mudah dibaca

✅ Tampilan Rapi – Hasil scan ditampilkan dalam tabel interaktif menggunakan Rich Library.


---

## 🔧Instalasi 

Sebelum menjalankan scanPARAM, pastikan Python dan library berikut sudah terinstal:

pip install requests beautifulsoup4 rich colorama


---
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
