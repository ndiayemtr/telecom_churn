from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_model_info():

    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert "model" in data
    assert "features_count" in data


def test_predict():

    payload = {
        "SeniorCitizen": 0,
        "tenure": 12,
        "MonthlyCharges": 70.5,
        "TotalCharges": 850.2,
        "gender": "Male",
        "Partner": "Yes",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check"
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "probability_churn" in data
    assert "prediction" in data