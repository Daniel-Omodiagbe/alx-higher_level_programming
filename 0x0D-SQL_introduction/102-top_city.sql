-- displays the top 3 of cities temperature during July and August
USE hbtn_0c_0;
SELECT city, AVG(value) AS "avg_temp" FROM temperatures
WHERE month = 7 OR month AND month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
