USE imdatabase
--NO 1
-- how to i show the emoployee who have job level SE SSE TL who have salary <50000
SELECT * FROM imdatabase.employee WHERE JobLevel IN ('SE','SSE','TL') AND Salary > 50000
 
-- NO 2
--display the records based on there tenure in the company, from longest to most recent
SELECT * FROM imdatabase.employee ORDER BY Hiredate ASC

-- NO 3
-- display EMPID,NAME, SALARY, JOBLEVEL of the refular empolyess sort by salary in highest to lowest
SELECT EmpNo, EmpName, JobLevel, Salary from imdatabase.employee Where Estatus ='R' ORDER BY Salary DESC


-- NO 4  
-- display the empid, name, salary, joblevel. Sort by job  level in ascending order and salary in descending order
SELECT EmpNo, EmpName, JobLevel,Salary from imdatabase.employee ORDER BY JobLevel ASC, Salary Desc

-- NO 5 
-- Display the salary of all the regular employees (R) who were hired between 2015 and 2018
SELECT Salary, EmpNo FROM imdatabase.employee WHERE Estatus ='R'AND Hiredate BETWEEN '2015-01-01' AND '2018-12-31'

--NO 6
-- Display record of employee in department 'OPN' if their salary is within 40k to 60k
SELECT * From imdatabase.employee 
WHERE DeptCode ='OPN' AND Salary Between 40000 AND 60000

--NO 7
--list the empnames which begins with the letter 'A' and end with the letter 'N'
ELECT EmpName FROM imdatabase.employee WHERE EmpName LIKE 'A%N'

-- display the record of those in 'OPN', SAL' and 'FIN' department sorted by department code in ascending order and salary in descending order
SELECT * FROM imdatabase.employee WHERE DeptCode IN ('OPN','SAL','FIN') ORDER BY DeptCode ASC, Salary DESC







