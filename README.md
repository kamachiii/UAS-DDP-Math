# 🧮 UAS-DDP-Math

**Aplikasi Kalkulator Matematika Berbasis Web**  
Project Ujian Akhir Semester - Dasar-Dasar Pemrograman

![Django](https://img.shields.io/badge/Django-5.1.4-green?style=flat&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 📖 Deskripsi Project

**UAS-DDP-Math** adalah aplikasi web kalkulator matematika yang dikembangkan menggunakan framework Django. Aplikasi ini menyediakan berbagai fitur perhitungan matematika dasar hingga geometri, termasuk operasi aritmatika, perhitungan bangun datar, dan bangun ruang.

Project ini dibuat sebagai tugas Ujian Akhir Semester untuk mata kuliah Dasar-Dasar Pemrograman, dengan tujuan mengimplementasikan konsep-konsep pemrograman Python dalam aplikasi web yang interaktif dan user-friendly.

---

## ✨ Fitur Utama

### 1. 🔢 Kalkulator Aritmatika
Operasi matematika dasar:
- ➕ Penjumlahan
- ➖ Pengurangan
- ✖️ Perkalian
- ➗ Pembagian

### 2. 📐 Bangun Datar
Perhitungan luas dan keliling untuk:
- 🟦 **Persegi** - Luas & Keliling
- 🟨 **Persegi Panjang** - Luas & Keliling
- 🔺 **Segitiga** - Luas & Keliling
- ⭕ **Lingkaran** - Luas & Keliling
- 🔷 **Jajar Genjang** - Luas & Keliling
- 🔶 **Trapesium** - Luas & Keliling

### 3. 🎲 Bangun Ruang
Perhitungan volume dan luas permukaan untuk:
- 📦 **Kubus** - Volume & Luas Permukaan
- 📦 **Balok** - Volume & Luas Permukaan
- 🔺 **Prisma Segitiga** - Volume & Luas Permukaan
- 🔲 **Prisma Segiempat** - Volume & Luas Permukaan
- ⬡ **Prisma Segienam** - Volume & Luas Permukaan
- 🥫 **Tabung** - Volume & Luas Permukaan
- 🔻 **Limas Segitiga** - Volume & Luas Permukaan
- 🔻 **Limas Segiempat** - Volume & Luas Permukaan

---

## 🛠️ Teknologi yang Digunakan

- **Backend Framework**: Django 5.1.4
- **Programming Language**: Python 3.x
- **Database**: SQLite3
- **Template Engine**: Django Templates
- **Frontend**: HTML, CSS, JavaScript

---

## 📋 Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal:

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Virtual environment (disarankan)

---

## 🚀 Cara Instalasi dan Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/kamachiii/UAS-DDP-Math.git
cd UAS-DDP-Math
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Migrasi Database
```bash
python manage.py migrate
```

### 5. Jalankan Server Development
```bash
python manage.py runserver
```

### 6. Akses Aplikasi
Buka browser dan akses:
```
http://127.0.0.1:8000/
```

---

## 📁 Struktur Project

```
UAS-DDP-Math/
│
├── calculator/                 # Aplikasi Django utama
│   ├── templates/              # Template HTML
│   ├── views.py                # Logic perhitungan matematika
│   ├── models.py               # Database models
│   └── apps.py                 # Konfigurasi aplikasi
│
├── math_project/               # Project settings
│   ├── settings.py             # Konfigurasi Django
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── db.sqlite3                  # Database SQLite
├── manage.py                   # Django management script
└── README.md                   # Dokumentasi project
```

---

## 🎯 Cara Penggunaan

1. **Pilih Menu**: Pada halaman utama, pilih jenis perhitungan yang ingin dilakukan (Aritmatika, Bangun Datar, atau Bangun Ruang)

2. **Input Data**: Masukkan nilai-nilai yang diperlukan pada form yang tersedia

3. **Hitung**: Klik tombol hitung untuk mendapatkan hasil

4. **Lihat Hasil**: Hasil perhitungan akan ditampilkan di halaman yang sama

---

## 📝 Lisensi

Project ini dibuat untuk keperluan akademik - UAS Dasar-Dasar Pemrograman.

---

## 🙏 Acknowledgments

- Terima kasih kepada dosen pengampu mata kuliah Dasar-Dasar Pemrograman
- Dokumentasi Django untuk referensi framework
- Komunitas Python Indonesia untuk dukungan pembelajaran

---

## 📞 Kontak & Support

Jika Anda memiliki pertanyaan atau saran, silakan:
- Buat [Issue](https://github.com/kamachiii/UAS-DDP-Math/issues) di repository ini
- Hubungi saya melalui GitHub

---

<div align="center">
  
**⭐ Jika project ini membantu, jangan lupa berikan star! ⭐**

Made with ❤️ for UAS DDP

</div>
