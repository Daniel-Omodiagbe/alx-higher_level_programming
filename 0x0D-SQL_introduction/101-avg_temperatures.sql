-- Import in hbtn_0c_0 database and find average of temperature

USE hbtn_0c_0;
SELECT city, AVG(value) AS "avg_temp" FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
