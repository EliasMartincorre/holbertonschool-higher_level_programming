-- CReate a table with foreing key, references state table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    state_id int NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256)
);