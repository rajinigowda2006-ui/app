CREATE DATABASE mydb;
USE mydb;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    price INT
);

INSERT INTO products (id,name, price) VALUES
(1,'Laptop', 150),
(2,'Mouse', 100),
(3,'USB cable', 50)
(4,'HP', 180)

;