-- CRea una base de datos y dentro de la misma una tabla.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
  id int NOT NULL AUTO_INCREMENT UNIQUE, 
  name VARCHAR(256)NOT NULL,
  PRIMARY KEY(id) 
);