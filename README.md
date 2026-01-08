# Proyek: Pemrosesan Data ETL Pipeline – Fashion Product Data

Deskripsi
---

Proyek ini merupakan implementasi **ETL (Extract, Transform, Load)** pipeline untuk mengambil data produk fashion dari sebuah website, membersihkan dan mentransformasikan data, lalu menyimpannya ke beberapa tujuan penyimpanan seperti **CSV**, **PostgreSQL**, dan **Google Sheets**.

Proyek ini dirancang sebagai bagian dari latihan *data engineering* yang mencakup web scraping, data cleaning, integrasi database, serta otomatisasi alur data.

---

## 🧩 Arsitektur ETL

1. **Extract**

   * Melakukan web scraping data produk dari:

     ```
     https://fashion-studio.dicoding.dev/
     ```
   * Mengambil data hingga **50 halaman** menggunakan `requests` dan `BeautifulSoup`.

2. **Transform**

   * Membersihkan data produk:

     * Normalisasi harga
     * Penyesuaian format teks
     * Penanganan data kosong atau tidak valid
   * Menggunakan `pandas` untuk manipulasi data.

3. **Load**

   * Menyimpan data hasil transformasi ke:

     * 📄 File CSV
     * 🐘 Database PostgreSQL
     * 📊 Google Sheets (menggunakan Google Sheets API)

---

## 📁 Struktur Proyek

```
.
├── main.py
├── requirements.txt
├── submission.txt
├── products.csv
├── google-sheets-api.json
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
└── tests/
    └── test_etl.py
```

---

## ⚙️ Teknologi yang Digunakan

* **Python 3**
* **Requests & BeautifulSoup** – Web Scraping
* **Pandas** – Data Processing
* **SQLAlchemy & Psycopg2** – PostgreSQL Integration
* **Google Sheets API** – Cloud Spreadsheet
* **Pytest & Coverage** – Unit Testing
* **Python Crontab** – Scheduling (opsional)

---

## 📦 Instalasi

1. Clone repository:

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Pastikan PostgreSQL sudah berjalan dan konfigurasi database sudah sesuai di modul `load.py`.

4. Pastikan file kredensial Google Sheets API tersedia:

```
google-sheets-api.json
```

---

## ▶️ Cara Menjalankan Program

Menjalankan proses ETL utama:

```bash
python main.py
```

---

## 🧪 Pengujian

Menjalankan unit test:

```bash
python -m unittest discover tests
```

Menjalankan test dengan coverage:

```bash
coverage run -m unittest discover tests
coverage report -m
```

---

## 📊 Hasil Output

* 📄 **CSV File**: `products.csv`
* 🐘 **PostgreSQL Table**: tersimpan otomatis
* 📊 **Google Sheets**:
  👉 [Lihat Spreadsheet](https://docs.google.com/spreadsheets/d/1udOdJigke9ffYoKAJvHwP0UOLVvEHgqIlTyzjseRDiM/edit?usp=sharing)

---

## 🚀 Pengembangan Selanjutnya

* Penjadwalan ETL otomatis menggunakan `cron`
* Logging dan error handling yang lebih detail
* Containerization menggunakan Docker
* Integrasi ke data warehouse (BigQuery / Redshift)

---

## 👨‍💻 Author

**Muchamad Aldi Firmansyah**
