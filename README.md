
## 🚀 HBW Scanner – Alat Pencari Parameter & Link di Website

##   🛠️ Fitur Utama
✅ **Scan Parameter URL** – Mencari parameter tersembunyi di link halaman.  
✅ **Grep Links & Resources** – Menampilkan semua link, gambar, CSS, dan JavaScript dari halaman target.  
✅ **Menampilkan jumlah total hasil** – Mempermudah analisis data yang ditemukan.  
✅ **Otomatis mengubah link relatif menjadi link absolut** agar mudah diakses.  
✅ **Tampilan lebih rapi dengan tabel berwarna** menggunakan Rich.  

---

## 📌 Instalasi Library
Sebelum menjalankan script, pastikan library berikut sudah terinstal:

```sh
pip install requests beautifulsoup4 rich


## 📜 Penjelasan Library:

requests → Mengambil halaman web (HTTP request).

beautifulsoup4 → Parsing HTML untuk ekstraksi data.

rich → Membuat output lebih keren dengan warna dan tabel.



---

🔧 Cara Menggunakan HBW Scanner

1️⃣ Jalankan script:

python scanPARAM.py

2️⃣ Pilih mode scan:

1 → Scan Parameter URL

2 → Scan Link & Resource (Grep Mode) + Ekstrak



---

## 📌 Contoh Hasil Scan

### Scan Link & Resource

| Jenis        | URL                                       |
|-------------|-------------------------------------------|
| 🔗 Link      | https://target.com/page.php?id=123       |
| 🖼️ Gambar    | https://target.com/media/logo.png       |
| 📜 JavaScript | https://target.com/assets/script.js     |
| 🎨 CSS       | https://target.com/style.css            |

**Total link dan resource ditemukan:** `3`

### Scan Parameter URL

| Parameter   | Urlnya Cuyy                                |
|------------|-------------------------------------------|
| id         | https://target.com/page.php?id=123       |
| search     | https://target.com/search.php?query=test |

**Total parameter ditemukan:** `3`

---

🔥 **HBW Scanner by hbwterminator** 🚀
