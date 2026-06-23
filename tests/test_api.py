from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict():
    payload = {
        "SeniorCitizen": 0,
        "tenure": 10,
        "MonthlyCharges": 70.0,
        "TotalCharges": 700.0,
        "gender_Male": True,
        "Partner_Yes": False,
        "Dependents_Yes": False,
        "PhoneService_Yes": True,
        "MultipleLines_Yes": False,
        "InternetService_Fiber_optic": True,
        "OnlineSecurity_Yes": False,
        "OnlineBackup_Yes": False,
        "DeviceProtection_Yes": False,
        "TechSupport_Yes": False,
        "StreamingTV_Yes": False,
        "StreamingMovies_Yes": False,
        "Contract_One_year": False,
        "Contract_Two_year": False,
        "PaperlessBilling_Yes": True,
        "PaymentMethod_Electronic_check": True
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()