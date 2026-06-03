from sqlalchemy import create_engine, text
import os
from datetime import datetime

def load_data(dim_waktu, fact_market, db_url):
    print("3. Memuat data ke PostgreSQL...")
    
    # [Data Dump / Archiving]
    archive_dir = os.path.join('data', 'archive')
    os.makedirs(archive_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dump_path = os.path.join(archive_dir, f"datadump_market_{timestamp}.csv")
    fact_market.to_csv(dump_path, index=False)
    
    engine = create_engine(db_url)
    
    # Wajib menghapus view lama sebelum menimpa tabel, jika tidak PostgreSQL akan error (Dependent Objects)
    with engine.connect() as conn:
        conn.execute(text("DROP MATERIALIZED VIEW IF EXISTS mv_market_summary CASCADE;"))
        conn.commit()
    
    # Proses Load (Mengirim DataFrame menjadi Tabel di Database)
    dim_waktu.to_sql('dim_waktu', engine, if_exists='replace', index=False)
    fact_market.to_sql('fact_market', engine, if_exists='replace', index=False)
    
    print("-> Load Data Selesai! Silakan jalankan query objek OLAP di pgAdmin.")