import mysql.connector


def get_connection():
    return mysql.connector.connect(host="localhost", user="root", database="loan_risk")


def get_loans():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM loan")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    cursor.close()
    conn.close()

    return rows, columns


def get_loan_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM loan_product")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    cursor.close()
    conn.close()

    return rows, columns


def get_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    cursor.close()
    conn.close()

    return rows, columns
