import pandas as pd


def calculate_product_risk(df, product_df):
    merged_df = df.merge(product_df, on="product_id")

    product_risk = merged_df.groupby("product_name").agg(
        total_loans=("loan_id", "count"),
        delinquent_loans=("loan_status", lambda x: (x == "연체").sum()),
    )

    product_risk["delinquency_rate"] = (
        product_risk["delinquent_loans"] / product_risk["total_loans"] * 100
    )

    return product_risk.reset_index()


def calculate_credit_risk(df):
    credit_risk = df.groupby("credit_grade").agg(
        total_loans=("loan_id", "count"),
        bad_loans=("loan_status", lambda x: (x == "부실").sum()),
    )

    credit_risk["bad_rate"] = (
        credit_risk["bad_loans"] / credit_risk["total_loans"] * 100
    )

    return credit_risk.reset_index()


def calculate_region_risk(df):
    region_risk = df.groupby("region").agg(
        total_loans=("loan_id", "count"),
        risky_loans=("loan_status", lambda x: x.isin(["연체", "부실"]).sum()),
    )

    region_risk["risk_rate"] = (
        region_risk["risky_loans"] / region_risk["total_loans"] * 100
    )

    return region_risk.reset_index()


def calculate_yearly_risk(df):
    yearly_risk = df.copy()

    yearly_risk["loan_date"] = pd.to_datetime(yearly_risk["loan_date"])

    yearly_risk["loan_year"] = yearly_risk["loan_date"].dt.year

    yearly_risk = yearly_risk.groupby("loan_year").agg(
        total_loans=("loan_id", "count"),
        risky_loans=("loan_status", lambda x: x.isin(["연체", "부실"]).sum()),
    )

    yearly_risk["risk_rate"] = (
        yearly_risk["risky_loans"] / yearly_risk["total_loans"] * 100
    )

    return yearly_risk.reset_index()


def find_anomalies(df):
    anomalies = df[df["delinquency_days"] >= 90].copy()

    anomalies["anomaly_reason"] = "90일 이상 장기 연체"

    return anomalies
