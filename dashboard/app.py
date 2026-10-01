import sys
import os

import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from database import get_loans, get_loan_products, get_customers

from analysis import (
    calculate_product_risk,
    calculate_credit_risk,
    calculate_region_risk,
    calculate_yearly_risk,
    find_anomalies,
)

st.title("Loan Risk Dashboard")

st.write("MySQL 연결 성공")


# =========================
# 데이터 불러오기
# =========================

rows, columns = get_loans()
df = pd.DataFrame(rows, columns=columns)

product_rows, product_columns = get_loan_products()
product_df = pd.DataFrame(product_rows, columns=product_columns)

customer_rows, customer_columns = get_customers()
customer_df = pd.DataFrame(customer_rows, columns=customer_columns)


# =========================
# 필터
# =========================

credit_grades = ["전체"] + sorted(df["credit_grade"].unique().tolist())

selected_grade = st.selectbox("신용등급", credit_grades)

if selected_grade != "전체":
    df = df[df["credit_grade"] == selected_grade]

df = df.merge(product_df[["product_id", "product_name"]], on="product_id", how="left")
df = df.merge(customer_df[["customer_id", "region"]], on="customer_id", how="left")

product_names = ["전체"] + sorted(df["product_name"].unique().tolist())
selected_product = st.selectbox("상품", product_names)

if selected_product != "전체":
    df = df[df["product_name"] == selected_product]

regions = ["전체"] + sorted(df["region"].unique().tolist())

selected_region = st.selectbox("지역", regions)

if selected_region != "전체":
    df = df[df["region"] == selected_region]

loan_statuses = ["전체"] + sorted(df["loan_status"].unique().tolist())

selected_status = st.selectbox("대출상태", loan_statuses)

if selected_status != "전체":
    df = df[df["loan_status"] == selected_status]


start_date = st.date_input("시작일", value=pd.to_datetime(df["loan_date"]).min())

end_date = st.date_input("종료일", value=pd.to_datetime(df["loan_date"]).max())

df["loan_date"] = pd.to_datetime(df["loan_date"])

df = df[(df["loan_date"].dt.date >= start_date) & (df["loan_date"].dt.date <= end_date)]

# =========================
# KPI
# =========================

total_loans = len(df)

total_balance = df["outstanding_balance"].sum()

delinquent_loans = (df["loan_status"] == "연체").sum()

risky_loans = df["loan_status"].isin(["연체", "부실"]).sum()


col1, col2, col3, col4 = st.columns(4)

col1.metric("전체 대출 건수", total_loans)

col2.metric("총 대출 잔액", f"{total_balance:,.0f}")

col3.metric("연체 대출 건수", delinquent_loans)

col4.metric("위험 대출 건수", risky_loans)


# =========================
# 전체 대출 데이터
# =========================

with st.expander("필터링된 대출 원본 데이터 보기"):
    st.dataframe(df)


# =========================
# 상품 / 신용등급 분석
# =========================

product_risk = calculate_product_risk(df)

credit_risk = calculate_credit_risk(df)

highest_risk_product = product_risk.loc[product_risk["delinquency_rate"].idxmax()]

st.metric("최고 연체율 상품", highest_risk_product["product_name"])
st.metric("최고 연체율", f"{highest_risk_product['delinquency_rate']:.1f}%")


col1, col2 = st.columns(2)


with col1:

    st.subheader("상품별 연체율")

    st.dataframe(product_risk)

    st.bar_chart(product_risk.set_index("product_name")["delinquency_rate"])


with col2:

    st.subheader("신용등급별 부실률")

    st.dataframe(credit_risk)

    st.bar_chart(credit_risk.set_index("credit_grade")["bad_rate"])


# =========================
# 지역 / 기간 분석
# =========================

region_risk = calculate_region_risk(df)

yearly_risk = calculate_yearly_risk(df)


col1, col2 = st.columns(2)


with col1:

    st.subheader("지역별 위험도")

    st.dataframe(region_risk)

    st.bar_chart(region_risk.set_index("region")["risk_rate"])


with col2:

    st.subheader("기간별 위험 추이")

    st.dataframe(yearly_risk)

    st.line_chart(yearly_risk.set_index("loan_year")["risk_rate"])


# =========================
# 이상치
# =========================

anomalies = find_anomalies(df)

st.subheader("이상치 데이터")

st.dataframe(anomalies)
