-- Creates table force_name with NOT NULL constraint
-- name column cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
