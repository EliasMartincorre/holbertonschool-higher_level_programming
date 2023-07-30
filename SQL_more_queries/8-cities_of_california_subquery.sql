-- selecto two data from table citi and select only where name = california
SELECT id, name FROM cities
WHERE state_id =
(
    SELECT id
    FROM states
    WHERE name = "California")
    GROUP BY id
    ORDER BY id ASC;
