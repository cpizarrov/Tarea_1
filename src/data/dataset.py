import pandas as pd

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet"

def load_taxi_data() -> pd.DataFrame:
    return pd.read_parquet(URL)

def load_taxi_data_full(year="2020"):
    dfs = []

    for month in range(1, 5):
        month_str = f"{month:02d}" 
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month_str}.parquet"
        print(f" Cargando {url}")
        df = pd.read_parquet(url)
        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    return full_df

target_col = "high_tip"