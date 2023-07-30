-- creat a new user if not exist, set password anda otorga select privilegs in DB hbnt-0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* to 'user_0d_2'@'localhost';
