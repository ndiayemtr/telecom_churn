import pandas as pd

def compute_kpis(df: pd.DataFrame):
    return {
        "total_customers": len(df),
        "churn_rate": float((df["Churn"] == "Yes").mean()),
        "avg_tenure": float(df["tenure"].mean()),
        "avg_monthly_charges": float(df["MonthlyCharges"].mean())
    }