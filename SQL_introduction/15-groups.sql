-- Count records by score
-- Groups records by score and counts occurrences
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
