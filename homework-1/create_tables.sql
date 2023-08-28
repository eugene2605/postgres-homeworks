-- SQL-команды для создания таблиц
CREATE TABLE IF NOT EXISTS customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(30) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id serial PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id) ON DELETE CASCADE,
	employee_id int REFERENCES employees(employee_id) ON DELETE CASCADE,
	order_date date NOT NULL,
	ship_city varchar(20) NOT NULL
)
