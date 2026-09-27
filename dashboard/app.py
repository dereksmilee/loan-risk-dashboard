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

rows, columns = get_loans()

df = pd.DataFrame(rows, columns=columns)

total_loans = len(df)

total_balance = df["outstanding_balance"].sum()

delinquent_loans = (df["loan_status"] == "연체").sum()

col1, col2, col3 = st.columns(3)

col1.metric("전체 대출 건수", total_loans)
col2.metric("총 대출 잔액", f"{total_balance:,.0f}")
col3.metric("연체 대출 건수", delinquent_loans)

st.dataframe(df)

product_rows, product_columns = get_loan_products()

product_df = pd.DataFrame(product_rows, columns=product_columns)

customer_rows, customer_columns = get_customers()

customer_df = pd.DataFrame(customer_rows, columns=customer_columns)

merged_df = pd.merge(df, product_df, on="product_id")
merged_df = pd.merge(merged_df, customer_df, on="customer_id")

product_risk = calculate_product_risk(df, product_df)

st.subheader("상품별 연체율")

st.dataframe(product_risk)

st.bar_chart(product_risk.set_index("product_name")["delinquency_rate"])

credit_risk = calculate_credit_risk(df)

st.subheader("신용등급별 부실률")
st.dataframe(credit_risk)
st.bar_chart(credit_risk.set_index("credit_grade")["bad_rate"])

region_risk = calculate_region_risk(df, customer_df)

st.subheader("지역별 위험도")

st.dataframe(region_risk)

st.bar_chart(region_risk.set_index("region")["risk_rate"])

yearly_risk = calculate_yearly_risk(df)

st.subheader("기간별 위험 추이")
st.dataframe(yearly_risk)
st.line_chart(yearly_risk.set_index("loan_year")["risk_rate"])

anomalies = find_anomalies(df)

st.subheader("이상치 데이터")
st.dataframe(anomalies)
