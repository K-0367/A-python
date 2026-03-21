create database GIET;
USE GIET;
CREATE TABLE giet (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    address VARCHAR(50),
    desig VARCHAR(50),
    salary INT,
    gender CHAR(1)
);
INSERT INTO giet VALUES
(101, 'aman', 'delhi', 'doctor', 25000, 'M'),
(102, 'naman', 'gunupur', 'teacher', 15000, 'M'),
(103, 'raman', 'rayagada', 'plumber', 15000, 'M'),
(104, 'Navi', 'raipur', 'nurse', 15000, 'F'),
(105, 'Pavi', 'raigarh', 'police', 25000, 'F'),
(106, 'Ankit', 'china', 'singer', 45000, 'M'),
(107, 'Umesh', 'vizag', 'dancer', 45000, 'M'),
(108, 'ramesh', 'bihar', 'manager', 25000, 'M'),
(109, 'mahesh', 'patna', 'thied', 55000, 'M');
SELECT * FROM giet;
SELECT name FROM giet;
SELECT name, address FROM giet;
SELECT * FROM giet
WHERE name = 'aman';
SELECT * FROM giet
WHERE address = 'delhi';
SELECT * FROM giet
WHERE gender = 'M';
SELECT * FROM giet
WHERE desig = 'doctor';
SELECT * FROM giet
WHERE salary = 15000;
SELECT * FROM giet
WHERE salary > 20000;
SELECT * FROM giet
WHERE salary < 30000;
SELECT * FROM giet
WHERE gender = 'M' AND salary > 20000;
SELECT * FROM giet
WHERE gender = 'F' OR address = 'raipur';
SELECT * FROM giet
WHERE name LIKE 'a%';
SELECT * FROM giet
WHERE name LIKE '%h';
SELECT * FROM giet
WHERE address LIKE '%pur%';
SELECT * FROM giet
ORDER BY name ASC;
SELECT * FROM giet
ORDER BY name;
SELECT * FROM giet
ORDER BY salary DESC;
SELECT COUNT(*) FROM giet
WHERE gender = 'M';
SELECT COUNT(*) AS total_males
FROM giet
WHERE gender = 'M';
