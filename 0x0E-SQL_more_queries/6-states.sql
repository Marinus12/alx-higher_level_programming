-- Creates the database hbtn_0d_usa and the table states on my MySQL server
-- id INT unique, auto-generated, can't be null and is  PRIMARY KEY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates a database
USE hbtn_0d_usa;
-- use a database
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
-- creates a table
