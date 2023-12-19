USE intro_sql;

SELECT id, company_name, country, city FROM customers;

SELECT company_name AS 'Company Name' FROM customers;

SELECT country FROM customers;

SELECT DISTINCT country FROM customers;

SELECT id, company_name AS 'Company', address, city, phone FROM customers;

SELECT id, address,  region, phone, country, city FROM customers
 WHERE country ='Germany';
 
 SELECT id, customer_id, order_date, shipper, freight FROM orders
 WHERE freight >=130; 
 
 SELECT * FROM orders
 WHERE order_date BETWEEN '2019-07-01' AND '2020-07-31'; 
 
 SELECT id,order_date,shipper, freight FROM orders
 WHERE order_date >='2019-03-24';
 
 SELECT * FROM customers
 WHERE company_name LIKE '1%';
 
 SELECT * FROM orders
 WHERE shipper IN ( 'United Package', 'Speedy Express');
 
 SELECT  id, company_name, city, region, country AS 'Country' FROM customers
 WHERE country='canada' AND region='BC';
 
 SELECT id,order_date, shipper, freight FROM orders
 WHERE order_date <='2019-07-04';
 
 SELECT * FROM orders
 WHERE order_date >= '2018-01-08' AND order_date <= '2020-12-31' ;
 
 SELECT id, order_date, shipper,freight FROM orders
 WHERE order_date BETWEEN '2018-05-06' AND '2020-07-03';
 
 SELECT * FROM orders
 WHERE shipper = 'United Package' OR shipper = 'Speedy Express';
 
 SELECT id, company_name, city, country FROM customers 
 ORDER BY country ASC;
 
 SELECT id, company_name, region, country FROM customers
   ORDER BY company_name DESC;
   
   SELECT * FROM customers
     ORDER BY country ASC, company_name DESC, region ASC; 
     
	SELECT product_name AS Product, category, unit_price AS Price FROM products
    WHERE units_in_stock > 20
    ORDER BY category ASC, unit_price DESC;
 
 SELECT * from customers
 GROUP BY country;
 
 SELECT * FROM products;
 
 SELECT category, units_in_stock FROM products;
 
 SELECT DISTINCT category,units_in_stock FROM products;
 
 SELECT category,units_in_stock FROM products
 GROUP BY category;
 
 SELECT category, sum(units_in_stock) FROM products
 GROUP BY category;
 
 SELECT category, sum(units_in_stock) AS 'Total Stocks' FROM products
 GROUP BY category;
 
 SELECT category, MIN(unit_price) AS ' min price' FROM products 
 GROUP BY category;
 
 SELECT category, COUNT(id) AS 'Total Products' FROM products
 GROUP BY category;
 
 SELECT category, MAX(unit_price) AS 'max price' FROM products
 GROUP BY category;
 
 SELECT category, AVG(unit_price) AS 'Avg Price' FROM products
 GROUP BY category;
 
 SELECT GROUP_CONCAT (DISTINCT (category) SEPARATOR ',') AS 'Categories ' FROM products;
 
 SELECT STDDEV (unit_price) AS 'STD DEVIATION' FROM products;
 
 SELECT category, SUM(units_in_stock) AS 'Total Stock' FROM products
 GROUP BY category
 HAVING SUM(units_in_stock) > 300 ;
 
 SELECT year( order_date) AS 'Year',SUM(freight ) AS 'Freight' FROM orders
 GROUP BY year(order_date);
 

 -- ALL ABOUT DATABASE CREATION
 CREATE DATABASE AwesomeDatabase;
  -- CAUTION!!! CAREFUL!!!!  
  DROP DATABASE AwesomeDatabase;
  DROP TABLE Awesome_table;
  
  CREATE DATABASE AwesomeDatabase;
  USE AwesomeDatabase;
  
   -- CREATING TABLES
   CREATE TABLE Awesome_employees (
   id INT NOT NULL AUTO_INCREMENT,
   First_name VARCHAR(255) NOT NULL,
   Last_name VARCHAR(255) NOT NULL,
   dept VARCHAR(255) NOT NULL, 
   PRIMARY KEY(id)
 );
 
 CREATE TABLE Awesome_customers(
 id INT NOT NULL AUTO_INCREMENT,
 company_name VARCHAR(255) NOT NULL,
 country VARCHAR(255),
 emp_id INT,
 PRIMARY KEY(id),
 FOREIGN KEY(emp_id) REFERENCES Awesome_employees(id)
);

USE intro_sql;
CREATE TABLE shipper(
id INT NOT NULL AUTO_INCREMENT,
shipper_name VARCHAR(255),
phone VARCHAR(255),
PRIMARY KEY(id)
);

SELECT * FROM shipper;

USE awesomedatabase;
INSERT INTO awesome_employees (First_name,Last_name,dept)
VALUES('kavin','muthukumar','IT'); 
INSERT INTO awesome_employees
VALUES(DEFAULT,'lalith','muthukumar','sales');

SELECT * FROM awesome_employees;

USE intro_sql;
INSERT INTO shipper(shipper_name,phone)
VALUES( 'speedy_express','555 235-453'),
('united_pacakage','555 545-657'),
('federal_shipping','555 654-765');
SELECT *FROM shipper;

SELECT employees.first_name,employees.dept,customers.company_name,customers.phone
FROM employees
INNER JOIN customers ON employee_id = customers.employee_id; 

SELECT employees.first_name,employees.dept,customers.company_name,customers.phone
FROM employees
LEFT JOIN customers ON employee_id = customers.employee_id;

SELECT employees.first_name,employees.dept,customers.company_name,customers.phone
FROM employees
RIGHT JOIN customers ON employee_id = customers.employee_id;

SELECT employees.first_name,employees.dept,customers.company_name,customers.phone
FROM employees
RIGHT JOIN customers ON employee_id=customers.employee_id
WHERE employees.first_name IS NULL; 

SELECT customers.company_name AS 'company',customers.country, orders.order_date AS 'OrderDate',orders.shipper,orders.freight
FROM customers
INNER JOIN orders ON customer_id = orders.customer_id;
 