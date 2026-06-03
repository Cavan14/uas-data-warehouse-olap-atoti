from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from datetime import datetime
import time
import os

def run_etl():
    folder_path = os.path.join('data', 'raw') 
    # HANYA AMBIL 2 DATA: BTC dan FED
    df_btc, df_fed = extract_data(folder_path)
    
    # HANYA TRANSFORMASI 2 DATA
    dim_waktu, fact_market = transform_data(df_btc, df_fed)
    
    DB_URL = 'postgresql://postgres:unesa123@localhost:5433/uas_dw_aset'

    load_data(dim_waktu, fact_market, DB_URL)

if __name__ == "__main__":
    while True:
        print(f"[{datetime.now()}] ETL START")

        run_etl()

        print(f"[{datetime.now()}] ETL DONE")
        print("Menunggu 10 menit...\n")

        time.sleep(600)