## Parámetros
features = numeric_feat + categorical_feat
EPS = 1e-7
target_col = "high_tip"

## Construcción de features 

numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    "work_hours",
    "pickup_minute",
    "passenger_count",
    "trip_distance",
    "trip_time",
    "trip_speed"
]

categorical_feat = [
    "PULocationID",
    "DOLocationID",
    "RatecodeID",
]
