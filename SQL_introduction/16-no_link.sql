-- List records excluding NULL names
-- Displays records where name is not empty
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
