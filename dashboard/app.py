from pathlib import Path

import joblib
import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Telecom Churn Analytics",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Telecom Churn Prediction & Analytics Dashboard")

# =========================
# LOAD DATA (optionnel mais recommandé)
# =========================

try:
    response = requests.get(f"{API_URL}/cache_data", timeout=5)
    
    # Sécurité : On vérifie si FastAPI a répondu avec succès (Code 200)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
    else:
        st.error(f"Erreur de l'API : Code statut {response.status_code}")
        df = pd.DataFrame() # DataFrame vide pour éviter de bloquer la suite du script

except requests.exceptions.RequestException as e:
    st.error(f"Impossible de se connecter à l'API FastAPI. Vérifie qu'elle est lancée ! Erreur : {e}")
    df = pd.DataFrame()

# =========================
# KPI GLOBALS
# =========================
st.subheader("📊 Global KPIs")


try:
    res = requests.get(f"{API_URL}/analytics", timeout=5)
    kpis = res.json()

    col1, col2, col3 = st.columns(3)

    col1.metric("Churn Rate", f"{kpis['churn_rate']*100:.2f}%")
    col2.metric("Avg Tenure", f"{kpis['avg_tenure']:.1f} months")
    col3.metric("Avg Monthly Charges", f"{kpis['avg_monthly_charges']:.2f} $")

except Exception:
    st.warning("API analytics not available")

st.divider()

# =========================
# CHURN DISTRIBUTION
# =========================
st.subheader("📉 Churn Distribution")

fig = px.histogram(
    df,
    x="Churn",
    color="Churn",
    title="Churn vs Non-Churn Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# CHURN ANALYSIS
# =========================
st.subheader("📌 Churn Insights")

col1, col2 = st.columns(2)

fig1 = px.box(df, x="Churn", y="tenure", color="Churn", title="Tenure vs Churn")
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.box(df, x="Churn", y="MonthlyCharges", color="Churn", title="Monthly Charges vs Churn")
col2.plotly_chart(fig2, use_container_width=True)

# =========================
# FEATURE IMPORTANCE (from saved model)
# =========================
st.subheader("🔥 Feature Importance (Model Insight)")

try:
    response = requests.get(
    f"{API_URL}/feature-importance"
    )

    feat_df = pd.DataFrame(response.json())

    fig = px.bar(
        feat_df,
        x="importance",
        y="feature",
        orientation="h"
    )

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.warning(f"Feature importance not available: {e}")

# =========================
# REAL TIME PREDICTION
# =========================
st.subheader("⚡ Customer Churn Simulation")

st.sidebar.header("Customer Profile")

senior = st.sidebar.selectbox("Senior Citizen", [0, 1])
tenure = st.sidebar.slider("Tenure", 0, 72, 12)
monthly = st.sidebar.slider("Monthly Charges", 10.0, 120.0, 70.0)
total = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1000.0)

contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.sidebar.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

if st.sidebar.button("Predict Churn Risk"):

    payload = {
        "SeniorCitizen": senior,
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "gender": "Male",
        "Partner": "Yes",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": internet,
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": payment
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=5
        )
        result = response.json()

        prob = result["probability_churn"]
        pred = result["prediction"]

        st.subheader("🔮 Prediction Result")

        col1, col2 = st.columns(2)

        col1.metric("Churn Probability", f"{prob*100:.2f}%")

        if pred == 1:
            col2.error("🚨 High Risk Customer")
            st.warning("Action: Offer discount / retention campaign / call center follow-up")
        else:
            col2.success("✅ Low Risk Customer")

    except Exception as e:
        st.error(f"API Error: {e}")

# =========================
# FOOTER INSIGHTS
# =========================
st.divider()

st.subheader("📌 Business Insights")

st.markdown("""
- Customers with **Month-to-month contracts** are more likely to churn  
- Higher **Monthly Charges** increase churn probability  
- Longer **Tenure** reduces churn risk significantly  
- Fiber optic internet users show higher churn tendency  
""")