import pandas as pd
from src.config import EPS
from src.features.build_features import features

## Carga de datos
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

## Variable target 
target_col = "high_tip"

## Limpieza 
def preprocess(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    df = df[df['fare_amount'] > 0].reset_index(drop=True)
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = df['tip_fraction'] > 0.2

    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (
        (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) &
        (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    )
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.seconds
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] + EPS)

    df = df[['tpep_dropoff_datetime'] + features + [target_col]]
    df[features + [target_col]] = df[features + [target_col]].astype("float32").fillna(-1.0)
    df[target_col] = df[target_col].astype("int32")

    return df.reset_index(drop=True)