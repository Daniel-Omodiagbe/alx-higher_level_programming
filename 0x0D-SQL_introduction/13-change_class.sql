-- remove all record with score <= 5

DELETE FROM second_table WHERE score <= 5
ORDER BY score DESC;
