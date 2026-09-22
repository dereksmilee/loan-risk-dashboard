# ERD 설계

## 1. 데이터 설계 목적

대출 데이터를 저장하고 분석하기 위해 고객, 대출 상품, 대출 정보를 분리하여 관리한다.

---

## 2. Customer

고객 정보를 저장한다.

| 컬럼명 | 데이터 의미 | Key |
|---|---|---|
| customer_id | 고객 식별자 | PK |
| age | 고객 연령 | |
| income | 연소득 | |
| employment_type | 고용 형태 | |
| region | 지역 | |

---

## 3. Loan Product

대출 상품 정보를 저장한다.

| 컬럼명 | 데이터 의미 | Key |
|---|---|---|
| product_id | 상품 식별자 | PK |
| product_name | 상품명 | |
| product_type | 상품 유형 | |

---

## 4. Loan

실제 실행된 대출 정보를 저장한다.

| 컬럼명 | 데이터 의미 | Key |
|---|---|---|
| loan_id | 대출 식별자 | PK |
| customer_id | 고객 식별자 | FK |
| product_id | 대출 상품 식별자 | FK |
| loan_amount | 최초 대출 금액 | |
| outstanding_balance | 현재 대출 잔액 | |
| interest_rate | 금리 | |
| credit_grade | 신용등급 | |
| loan_date | 대출 실행일 | |
| maturity_date | 만기일 | |
| delinquency_days | 연체 일수 | |
| loan_status | 대출 상태 | |

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

- Customer 1명은 여러 개의 Loan을 가질 수 있다.
- 하나의 Loan은 하나의 Customer에 속한다.
- 하나의 Loan Product는 여러 개의 Loan에서 사용될 수 있다.
- 하나의 Loan은 하나의 Loan Product에 속한다.

---

## 6. Key 정의

### Primary Key (PK)

각 데이터를 고유하게 식별하기 위한 키이다.

- Customer → customer_id
- Loan Product → product_id
- Loan → loan_id

### Foreign Key (FK)

다른 테이블의 Primary Key를 참조하여 테이블 간 관계를 표현한다.

- Loan.customer_id → Customer.customer_id
- Loan.product_id → Loan Product.product_id
```

저장하고 나서 **아직 커밋하지 마.**

이번에는 우리가 처음으로 **"문서 → DB 설계"를 실제로 수정한 거라서**, 저장한 다음:

```bash
git status
```

만 쳐봐.

그러면 `docs/erd.md`가

```text
modified: docs/erd.md
```

라고 나올 거야.

**여기까지만 하고 결과 보여줘.**

그 다음에 내가 **PK/FK가 실제로 DB에서 어떻게 동작하는지** 예시 데이터를 넣어서 보여주고, 그 다음에 MySQL 테이블 설계로 넘어가자.