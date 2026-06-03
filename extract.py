import pandas as pd
import glob
import os

def extract_data(folder_path):
    print("1. Mengekstrak data BTC dan FED...")
    # Ekstrak Bitcoin
    all_btc = glob.glob(os.path.join(folder_path, "btc_usdt_kucoin_*.csv"))
    df_btc = pd.concat([pd.read_csv(f) for f in all_btc], ignore_index=True)
    df_btc['datetime'] = pd.to_datetime(df_btc['datetime'], utc=True)
    
    # Ekstrak Data The Fed
    fed_path = os.path.join(folder_path, "fed_economic_data_2018_2025.csv")
    df_fed = pd.read_csv(fed_path)
    df_fed['Date'] = pd.to_datetime(df_fed['Date'])
    
    return df_btc, df_fed