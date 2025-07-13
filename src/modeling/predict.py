import joblib
import pandas as pd
from sklearn.metrics import f1_score
from src.features.build_features import features
from src.data.dataset import load_taxi_data_full, target_col, preprocess


def load_model(path="models/random_forest.joblib"):
    return joblib.load(path)

def predict(model, X):
    return model.predict_proba(X)

def evaluate(pred_probs, y_true):
    pred_labels = [p[1] for p in pred_probs.round()]
    return f1_score(y_true, pred_labels)

def evaluate_months(model, df, year="2020", start_month=1, end_month=12):
    df = df.copy()
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    results = []

    for month in range(start_month, end_month + 1):
        df_month = df[df["tpep_dropoff_datetime"].dt.month == month]

        if df_month.empty:
            continue

        X = df_month[features]
        y_true = df_month[target_col]

        pred_probs = predict(model, X)
        score = evaluate(pred_probs, y_true)

        results.append({
            "mes": f"{year}-{month:02d}",
            "n_casos": len(df_month),
            "f1_score": round(score, 4)
        })

    return pd.DataFrame(results)