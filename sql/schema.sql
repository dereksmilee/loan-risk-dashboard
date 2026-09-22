CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    age INT,
    income DECIMAL(12, 2),
    employment_type VARCHAR(50),
    region VARCHAR(50)
);


CREATE TABLE loan_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_type VARCHAR(50)
);

CREATE TABLE loan (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    loan_amount DECIMAL(12, 2),
    outstanding_balance DECIMAL(12, 2),
    interest_rate DECIMAL(5, 2),
    credit_grade VARCHAR(10),
    loan_date DATE,
    maturity_date DATE,
    delinquency_days INT,
    loan_status VARCHAR(20),

    FOREIGN KEY (customer_id)
        REFERENCES customer(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES loan_product(product_id)
);