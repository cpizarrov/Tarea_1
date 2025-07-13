import pandas as pd

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet"

def load_taxi_data() -> pd.DataFrame:
    return pd.read_parquet(URL)


