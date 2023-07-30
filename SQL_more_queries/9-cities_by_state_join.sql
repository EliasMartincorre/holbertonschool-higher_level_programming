-- Left join 
SELECT c.id, c.name, s.name 
FROM states AS s 
LEFT JOIN cities AS c 
ON s.id = c.state_id
ORDER BY c.id asc;