-- crea una tabla con un numero de id unico
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name VARCHAR(256)
) ;