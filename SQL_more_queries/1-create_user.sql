-- creat a new user if not exist, set password anda otorga all privilegs in mysql server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES on *.* to 'user_0d_1'@'localhost';