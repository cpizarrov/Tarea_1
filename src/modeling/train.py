from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X, y, n_estimators=100, max_depth=10, save_path="models/random_forest.joblib"):
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X, y)
    joblib.dump(model, save_path)
    return model
