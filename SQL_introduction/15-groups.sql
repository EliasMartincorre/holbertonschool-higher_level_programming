-- list number of records whit the same score in the table.
SELECT score, COUNT(id) as "number"
FROM second_table
GROUP BY score
ORDER BY score DESC;
