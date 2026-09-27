# 시스템 아키텍처

## 1. 시스템 개요

Loan Risk Dashboard는 MySQL에 저장된 대출 데이터를 Python으로 조회하고 분석한 뒤, Streamlit을 통해 분석 결과를 제공하는 데이터 분석 대시보드이다.

---

## 2. 시스템 구성

```text
사용자
  ↓
Streamlit Dashboard
  ↓
Python
  ├── database.py
  │      ↓
  │    MySQL
  │
  └── analysis.py
         ↓
      데이터 분석
```

---

## 3. 주요 구성 요소

### Streamlit Dashboard

사용자가 대출 데이터를 확인하고 필터를 적용하며 분석 결과를 확인하는 화면을 제공한다.

주요 기능:

- 신용등급 필터
- 지역 필터
- 기간 필터
- 대출 현황 KPI
- 상품별 연체율
- 신용등급별 부실률
- 지역별 위험도
- 기간별 위험 추이
- 이상치 데이터 조회

### database.py

MySQL 데이터베이스와 애플리케이션 사이의 데이터 조회를 담당한다.

주요 역할:

- MySQL 연결
- 대출 데이터 조회
- 대출 상품 데이터 조회
- 고객 데이터 조회

### analysis.py

조회된 데이터를 기반으로 대출 위험도를 계산한다.

주요 역할:

- 상품별 연체율 계산
- 신용등급별 부실률 계산
- 지역별 위험도 계산
- 기간별 위험도 계산
- 이상치 탐색

### MySQL

대출 분석에 필요한 원천 데이터를 저장한다.

주요 테이블:

- customer
- loan_product
- loan

---

## 4. 데이터 처리 흐름

```text
MySQL
  ↓
database.py
  ↓
Pandas DataFrame
  ↓
필터링
  ↓
analysis.py
  ↓
위험지표 계산
  ↓
Streamlit
  ↓
사용자에게 결과 제공
```

---

## 5. 역할 분리

각 구성 요소는 하나의 역할에 집중하도록 분리한다.

| 구성 요소 | 주요 역할 |
|---|---|
| Streamlit | 사용자 화면 및 입력 처리 |
| database.py | 데이터베이스 조회 |
| analysis.py | 데이터 분석 및 위험지표 계산 |
| MySQL | 데이터 저장 |
| Pandas | 데이터 처리 |
