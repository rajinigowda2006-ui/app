CREATE DATABASE mydb;
USE mydb;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    price INT
);

INSERT INTO products (id,name, price) VALUES
(6,'Laptop', 150),
(7,'Mouse', 100),
(8,'USB cable', 50),
(9,'HP', 180),
(10,'dell',130);