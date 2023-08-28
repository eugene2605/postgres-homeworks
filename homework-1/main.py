"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os
# from dotenv import dotenv_values


password = os.getenv('PASSWORD_POSTGRES')
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=password)
try:
    with conn:
        with conn.cursor() as cur:

            with open('north_data\customers_data.csv', encoding='windows-1251') as customers_csv:
                customers = csv.DictReader(customers_csv)
                for customer in customers:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (customer['customer_id'], customer['company_name'], customer['contact_name']))

            with open('north_data\employees_data.csv', encoding='windows-1251') as employees_csv:
                employees = csv.DictReader(employees_csv)
                for employee in employees:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (employee['employee_id'], employee['first_name'], employee['last_name'],
                                 employee['title'], employee['birth_date'], employee['notes']))

            with open('north_data\orders_data.csv', encoding='windows-1251') as orders_csv:
                orders = csv.DictReader(orders_csv)
                for order in orders:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (order['order_id'], order['customer_id'], order['employee_id'],
                                 order['order_date'], order['ship_city']))

finally:
    conn.close()
