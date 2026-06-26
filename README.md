# 📞 Telecom Customer Churn Prediction

End-to-end Data Science project for predicting telecom customer churn.

---

## 🚀 Live Demo

### 📊 Streamlit Dashboard

https://telecomchurn-ks4yvxhrvmyimaxhq567jd.streamlit.app/

### ⚡ FastAPI

https://telecom-churn-7q6x.onrender.com

API Documentation

https://telecom-churn-7q6x.onrender.com/docs

---

# Project Architecture

```
User
      │
      ▼
Streamlit Dashboard
      │
 REST API
      │
      ▼
FastAPI
      │
Machine Learning Model
(Random Forest)
```

---

# Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Streamlit
* Plotly
* Docker
* Docker Compose
* Pytest
* GitHub Actions
* Render
* Streamlit Community Cloud

---

# Dataset

Telco Customer Churn Dataset

* 7,043 customers
* 21 original variables
* Binary classification (Churn / No Churn)

---

# Machine Learning Pipeline

* Data Cleaning
* Missing Values Processing
* Feature Engineering
* One-Hot Encoding
* Train/Test Split
* Random Forest Classifier
* Model Evaluation
* Model Serialization

---

# Model Performance

Random Forest

| Metric            | Score |
| ----------------- | ----- |
| Accuracy          | 79%   |
| ROC AUC           | 0.82  |
| Precision (Churn) | 0.63  |
| Recall (Churn)    | 0.51  |

---

# API Endpoints

## Health

GET

```
/health
```

---

## Prediction

POST

```
/predict
```

Example

```json
{
    "SeniorCitizen":0,
    "tenure":12,
    "MonthlyCharges":70,
    "TotalCharges":850,
    "gender":"Male",
    "Partner":"Yes",
    "Dependents":"No",
    "PhoneService":"Yes",
    "MultipleLines":"No",
    "InternetService":"Fiber optic",
    "OnlineSecurity":"No",
    "OnlineBackup":"No",
    "DeviceProtection":"No",
    "TechSupport":"No",
    "StreamingTV":"No",
    "StreamingMovies":"No",
    "Contract":"Month-to-month",
    "PaperlessBilling":"Yes",
    "PaymentMethod":"Electronic check"
}
```

Response

```json
{
    "probability_churn":0.81,
    "prediction":1
}
```

---

# Dashboard Features

* KPI Overview
* Churn Distribution
* Churn Insights
* Feature Importance
* Customer Simulation
* Live Prediction via FastAPI

---

# Docker

Run locally

```
docker compose up --build
```

Dashboard

```
http://localhost:8501
```

API

```
http://localhost:8000/docs
```

---

# CI/CD

GitHub Actions automatically executes

* Unit Tests
* Build Validation

Every push to the repository triggers the workflow.

---

# Deployment

FastAPI

Render

Dashboard

Streamlit Community Cloud

---

# Project Structure

```
telecom_churn/

│
├── app/
├── dashboard/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
├── .github/workflows/
├── Dockerfile.api
├── Dockerfile.dashboard
├── docker-compose.yml
├── requirements-api.txt
├── requirements-dashboard.txt
└── README.md
```

---

# Future Improvements

* XGBoost Model
* LightGBM
* SHAP Explainability
* MLflow Model Registry
* PostgreSQL Database
* Authentication
* Kubernetes Deployment
* Monitoring with Prometheus & Grafana

---

# Author

**Matar Ndiaye**

Data Scientist | Machine Learning Engineer | Data Analyst

GitHub:
https://github.com/ndiayemtr
