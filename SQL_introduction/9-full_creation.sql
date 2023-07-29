-- create a second_table and insert tree new row
CREATE TABLE IF NOT EXISTS second_table(
        id int not null,
        name varchar(256) not null,
        score int not null
);

INSERT INTO second_table (id, name, score)
values
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);

