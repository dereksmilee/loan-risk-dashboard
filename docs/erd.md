# ERD 설계

## 1. 데이터 설계 목적

대출 데이터를 저장하고 분석하기 위해 필요한 테이블과 컬럼을 정의한다.

---

## 2. 핵심 데이터

### Loan

대출 정보를 저장한다.

| 컬럼명 | 설명 |
|---|---|
| loan_id | 대출 식별자 |
| customer_id | 고객 식별자 |
| product_id | 대출 상품 식별자 |
| loan_amount | 최초 대출 금액 |
| outstanding_balance | 현재 대출 잔액 |
| interest_rate | 금리 |
| credit_grade | 신용등급 |
| region | 지역 |
| loan_date | 대출 실행일 |
| maturity_date | 만기일 |
| delinquency_days | 연체 일수 |
| loan_status | 대출 상태 |

---

## 3. 대출 상품

### Loan Product

| 컬럼명 | 설명 |
|---|---|
| product_id | 상품 식별자 |
| product_name | 상품명 |
| product_type | 상품 유형 |

---

## 4. 고객

### Customer

| 컬럼명 | 설명 |
|---|---|
| customer_id | 고객 식별자 |
| age | 연령 |
| income | 연소득 |
| employment_type | 고용 형태 |
| region | 지역 |

---

## 5. 테이블 관계

```text
Customer
   │
   │ 1:N
   ↓
Loan
   │
   │ N:1
   ↓
Loan Product
```

한 명의 고객은 여러 개의 대출을 보유할 수 있다.

하나의 대출은 하나의 대출 상품에 속한다.