import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "model.pkl")
features = joblib.load(BASE_DIR / "features.pkl")


def preprocess(data):
    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=features, fill_value=0)

    return df


def predict(data):
    df = preprocess(data)

    proba = model.predict_proba(df)[0][1]
    pred = int(proba > 0.5)

    return {
        "probability_churn": float(proba),
        "prediction": pred
    }

def load_model_data():
    return {
        "model": model,
        "features": features
    }