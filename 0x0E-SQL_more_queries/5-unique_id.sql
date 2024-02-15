-- Script that creates the table unique_id on my MySQL server.
-- id INT with default value 1 and must be unique
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (Id INT DEFAULT 1 UNIQUE, VARCHAR(256));
