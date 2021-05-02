-- Question 2.1
SELECT name FROM records WHERE supervisor="Oliver Warbucks";

-- Question 2.2
SELECT * FROM records WHERE name=supervisor;

-- Question 2.3
SELECT name FROM records WHERE salary>50000 ORDER BY name;

-- Question 3.1
SELECT b.day, b.time FROM records AS a, meetings AS b
WHERE a.division = b.division;

-- Question 3.2
SELECT a.name, b.name FROM records AS a, records AS b
WHERE a.division = b.division and a.name < b.name;

-- Question 3.3
SELECT "Will."

-- Question 3.4
SELECT a.name FROM records AS a, records AS b
WHERE a.supervisor = b.name and a.division <> b.division;

-- Question 4.1
SELECT supervisor, SUM(salary) FROM records
GROUP BY supervisor

-- Question 4.2
SELECT day FROM records AS a, meetings AS b
WHERE a.division = b.division
GROUP BY day
HAVING COUNT(*) < 5;

-- Question 4.3
SELECT division FROM records
GROUP BY division
HAVING SUM(salary) < 100000;

-- Question 5.1
CREATE TABLE num_taught AS
SELECT Professor, Course, COUNT(*) AS times
FROM courses
GROUP BY Professor, Course

-- Question 5.2
SELECT a.Professor, b.Professor, a.Course
FROM courses AS a, courses AS b
WHERE a.Professor <> b.Professor
GROUP BY a.Course
HAVING COUNT(a.times) = COUNT(b.times)

-- Question 5.3
SELECT a.Professor, b.Professor
FROM courses AS a, courses AS b
WHERE a.Professor <> b.Professor
GROUP BY a.Course
HAVING COUNT(a.times) > 2;




