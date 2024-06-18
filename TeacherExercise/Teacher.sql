USE imdatabase;
SELECT * FROM imdatabase.teacher;

-- 1. Display the sum of salary for each status if the sum is less than 300000

SELECT Estatus, SUM(Salary) AS TotalSalary
FROM teacher
GROUP BY Estatus   -- GROUP BY Status: Groups the results by Status
HAVING SUM(SALARY) <300000;   -- HAVING SUM(Salary) < 300000: Filters the grouped results to include only those where the total salary sum is less than 300,000.

-- 2. What is the minimum and maximum salary of faculty members for each level. Do not include the part-timers.

SELECT  College, MIN(Salary) AS MinSalary, MAX(Salary) AS MaxSalary, Estatus
FROM teacher
GROUP BY College, Estatus
HAVING Estatus NOT IN ('Part-Timer');

-- 3. What is the total salary paid in each college. Display only the totals which fall between the 50k to 70k range. Display in ascending order of the total salary.

SELECT College, SUM(Salary) AS TotalSalary
FROM teacher
GROUP BY College
HAVING TotalSalary BETWEEN 50000 AND 70000; -- Filters the grouped result to include only those college salary is between 50k to 70k


-- 4. Count how many faculty members there are per level in each college
-- 4.1 Revise #2 to include only those hired during the years 2015 and 2020
SELECT College, Level, COUNT(*) As Members
FROM teacher
WHERE hiredate BETWEEN '2015-01-01' AND '2020-12-31'
GROUP BY College, Level;

-- 5. Sum up the salary per status in each college only for instructor levels (those whose level starts with ‘Inst’)
SELECT College, Estatus, SUM(Salary) As TotalSalary
from teacher
WHERE Level LIKE '%Inst%' -- Filters the results to include only those whose level starts with 'Inst'
GROUP BY College,Estatus;

-- 6. What is the average salary paid per level in each college. Do not include those in the professor level.
SELECT College,ROUND (AVG(Salary),2) AS AverageSalary
FROM teacher
WHERE Level NOT LIKE '%Prof%'
GROUP BY College
ORDER BY AverageSalary DESC;

-- 7. Count how many were hired during the month of January. 
SELECT TeacherName, COUNT(hiredate) AS JanuaryEmployees
FROM teacher
WHERE MONTH(hiredate) = 1
GROUP BY TeacherName;

-- 8. Count how many were hired per month.
SELECT YEAR(hiredate) AS Year, MONTH(hiredate) AS Month, COUNT(hiredate) AS HiresCount -- YEAR(hiredate) and MONTH(hiredate) extracts the year and month from the hiredate column
FROM teacher
GROUP BY YEAR(hiredate), MONTH(hiredate)
ORDER BY Year, Month; 
