from pathlib import Path

from fastapi import FastAPI
from app.schemas import CustomerInput
from app.utils import predict, load_model_data
from app.analytics import compute_kpis
import pandas as pd

app = FastAPI(title="Telecom Churn API", version="2.0")

BASE_DIR = Path(__file__).resolve().parent
# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}

# =========================
# PREDICTION
# =========================
@app.post("/predict")
def predict_churn(data: CustomerInput):
    return predict(data.dict())

# =========================
# MODEL INFO
# =========================
@app.get("/model-info")
def model_info():
    return {
        "model": "RandomForestClassifier",
        "version": "1.0",
        "features_count": len(load_model_data()["features"])
    }

# =========================
# ANALYTICS (SIMULATED DATA)
# =========================
@app.get("/analytics")
def analytics():
    df = pd.read_csv(BASE_DIR / "data.csv")  # plus tard: DB
    return compute_kpis(df)

@app.get("/cache_data")
def cache_data():
    df = pd.read_csv(BASE_DIR / "data.csv")

    return df.to_dict(orient="records")

@app.get("/feature-importance")
def feature_importance():

    model = load_model_data()["model"]
    features = load_model_data()["features"]

    importance = pd.DataFrame({
        "feature": features,
        "importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="importance",
        ascending=False
    ).head(15)

    return importance.to_dict(orient="records")