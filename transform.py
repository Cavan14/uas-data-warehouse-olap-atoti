import pandas as pd

def transform_data(df_btc, df_fed):

    print("2. Mentransformasi dan menggabungkan data...")

    # ======================
    # CLEAN BTC
    # ======================
    btc_clean = df_btc[['datetime', 'close', 'volume']].copy()
    btc_clean['date'] = btc_clean['datetime'].dt.tz_localize(None).dt.floor('D')
    btc_clean.rename(columns={'close': 'btc_close', 'volume': 'btc_volume'}, inplace=True)

    btc_clean = btc_clean.groupby('date').last().reset_index()

    # ======================
    # CLEAN FED
    # ======================
    fed_clean = df_fed[['Date', 'Fed_Funds_Rate']].copy()
    fed_clean['date'] = fed_clean['Date'].dt.floor('D')
    fed_clean.rename(columns={'Fed_Funds_Rate': 'fed_rate'}, inplace=True)

    fed_clean = fed_clean.groupby('date').last().reset_index()

    # ======================
    # JOIN
    # ======================
    df_merge = pd.merge(btc_clean, fed_clean, on='date', how='left')
    df_merge.sort_values('date', inplace=True)
    df_merge.ffill(inplace=True)
    df_merge.dropna(inplace=True)

    # ======================
    # DIMENSION TABLE
    # ======================
    dim_waktu = pd.DataFrame({
        'tanggal_lengkap': pd.to_datetime(df_merge['date'].unique())
    })

    dim_waktu['id_waktu'] = dim_waktu['tanggal_lengkap'].dt.strftime('%Y%m%d').astype(int)
    dim_waktu['nama_hari'] = dim_waktu['tanggal_lengkap'].dt.day_name()
    dim_waktu['kuartal'] = "Q" + dim_waktu['tanggal_lengkap'].dt.quarter.astype(str)
    dim_waktu['is_weekend'] = dim_waktu['tanggal_lengkap'].dt.dayofweek >= 5

    # ======================
    # FACT TABLE (FIXED)
    # ======================
    fact_market = pd.DataFrame({
        "id_waktu": df_merge['date'].dt.strftime('%Y%m%d').astype(int),
        "btc_close": df_merge['btc_close'],
        "btc_volume": df_merge['btc_volume'],
        "fed_rate": df_merge['fed_rate']
    })

    # feature engineering (ONLY ONCE)
    fact_market["tren_pasar_btc"] = fact_market["btc_close"].apply(
        lambda x: "Bullish" if x > 30000 else "Bearish"
    )

    return dim_waktu, fact_market