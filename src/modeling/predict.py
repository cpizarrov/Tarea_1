import joblib
from sklearn.metrics import f1_score

def load_model(path="models/random_forest.joblib"):
    return joblib.load(path)

def predict(model, X):
    return model.predict_proba(X)

def evaluate(pred_probs, y_true):
    pred_labels = [p[1] for p in pred_probs.round()]
    return f1_score(y_true, pred_labels)
