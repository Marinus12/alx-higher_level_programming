-- Lists all records of the table second_table of the database in my MySQL server
SELECT score, name
FROM secod_table
WHERE name != ""
ORDER BY score DESC;