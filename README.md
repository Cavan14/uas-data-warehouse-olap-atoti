# 📊 Data Warehouse & OLAP: Analisis Korelasi Bitcoin dan Suku Bunga FED
link dataset: https://www.kaggle.com/datasets/akmaleyzal/bitcoin-gold-and-the-fed-historical-data

Proyek ini merupakan implementasi *Data Warehouse* end-to-end yang mengintegrasikan data historis aset *cryptocurrency* (Bitcoin) dari KuCoin dengan data indikator makroekonomi (*Federal Funds Rate*) periode 2018–2025.

## 🚀 Arsitektur Sistem
Proyek ini mengadopsi pendekatan **Star Schema** dengan komponen berikut:
1. **ETL Pipeline (Python):** Ekstraksi *datadump* dinamis, penyesuaian *time granularity*, dan imputasi data *missing values* secara otomatis.
2. **Data Warehouse (PostgreSQL):** Repositori utama yang dilengkapi *Advanced Objects* berupa B-Tree Indexing dan Materialized View untuk mempercepat kueri analitik.
3. **OLAP Engine (Atoti):** Pemrosesan multidimensi (*Cube*) dan deteksi anomali volatilitas harga Bitcoin secara interaktif via dasbor.

## 📁 Struktur Folder
- `/data`: Berisi *datadump* mentah (CSV) dan hasil arsip ETL.
- `/src`: Skrip Python untuk proses Extract, Transform, dan Load (ETL).
- `Olap.sql`: Kueri DDL PostgreSQL untuk pembentukan fitur lanjut.
- `atoti.ipynb`: Jupyter Notebook untuk mesin OLAP dan visualisasi.
- `run_etl.py`: Skrip orkestrator automasi ETL.

## 🛠️ Tools & Teknologi
* **Bahasa:** Python 3.x, SQL
* **Library:** Pandas, SQLAlchemy, Glob, Schedule
* **Database:** PostgreSQL (pgAdmin 4)
* **Analitik:** Atoti, Jupyter Notebook
