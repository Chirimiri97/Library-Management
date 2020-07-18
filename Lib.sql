CREATE DATABASE books;
USE books;
CREATE TABLE books_info(
id INT PRIMARY KEY AUTO_INCREMENT,
book_name VARCHAR(100),
book_year INT,
book_author VARCHAR(100));