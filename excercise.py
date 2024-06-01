import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="imdatabase" # create database mydatabase
)

mycursor = mydb.cursor() # Create a cursor object using the cursor() method

# mycursor.execute("CREATE DATABASE imdatabase") # Create a database named "mydatabase"


#create table employee (EmpNo int, EmpName varchar(255), Salary int, JobLevel varchar(255), DeptCode varchar(255), Estatus varchar(255), Hiredate date)


# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (1, 'Akiko Thompson', 100000, 'MGR', 'ISD', 'R', '2010-01-16')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (2, 'Miki Mami', 120000, 'MGR', 'FIN', 'R', '2019-01-17')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (3, 'Chigu Suzuki', 115000, 'MGR', 'OPN', 'R', '2020-01-18')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (4, 'Hanae Kobayashi', 140000, 'MGR', 'SAL', 'P', '2021-04-19')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (5, 'Atsuko Celdran', 60000, 'AM', 'ISD', 'P', '2021-05-20')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (6, 'Yoko Cruz', 50000, 'TL', 'OPN', 'P', '2021-03-21')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (7, 'Reiko Carpenter', 50000, 'TL', 'SAL', 'C', '2018-01-22')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (8, 'Aikiko Melendez', 50000, 'TL', 'FIN', 'C', '2018-05-23')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (9, 'Kenra Reyes', 55000, 'AM', 'ISD', 'C', '2017-02-24')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (10, 'Mischka Laserna', 65000, 'AM', 'FIN', 'R', '2018-01-25')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (11, 'Jenny Balayas', 40000, 'SSE', 'SAL', 'R', '2018-01-26')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (12, 'Carmen Balagtas', 35000, 'SE', 'OPN', 'R', '2019-01-27')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (13, 'Jeanne Manio', 40000, 'SE', 'OPN', 'P', '2021-04-28')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (14, 'Christopher Rivo', 50000, 'TL', 'SAL', 'P', '2021-06-29')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (15, 'Janet Japson', 55000, 'AM', 'FIN', 'C', '2014-01-30')")
# mycursor.execute("INSERT INTO employee (EmpNo, EmpName, Salary, JobLevel, DeptCode, Estatus, Hiredate) VALUES (16, 'Julio Ignacio', 45000, 'SSE', 'ISD', 'R', '2015-01-31')")

# mydb.commit() # Commit your changes in the database

# # NO 1
# # how to i show the emoployee who have job level SE SSE TL who have salary <50000
# SELECT * FROM imdatabase.employee WHERE JobLevel IN ('SE','SSE','TL') AND Salary > 50000
 
# # NO 2
# #display the records based on there tenure in the company, from longest to most recent
# SELECT * FROM imdatabase.employee ORDER BY Hiredate ASC

# # NO 3
# # display EMPID,NAME, SALARY, JOBLEVEL of the refular empolyess sort by salary in highest to lowest
# SELECT EmpNo, EmpName, JobLevel, Salary from imdatabase.employee Where Estatus ='R' ORDER BY Salary DESC


# # NO 4  
# # display the empid, name, salary, joblevel. Sort by job  level in ascending order and salary in descending order
# SELECT EmpNo, EmpName, JobLevel,Salary from imdatabase.employee ORDER BY JobLevel ASC, Salary Desc

# # NO 5 
# # Display the salary of all the regular employees (R) who were hired between 2015 and 2018
# SELECT Salary, EmpNo FROM imdatabase.employee WHERE Estatus ='R'AND Hiredate BETWEEN '2015-01-01' AND '2018-12-31'

# NO 6
# # Display record of employee in department 'OPN' if their salary is within 40k to 60k
# SELECT * From imdatabase.employee 
# WHERE DeptCode ='OPN' AND Salary Between 40000 AND 60000

# NO 7
# #list the empnames which begins with the letter 'A' and end with the letter 'N'
# SELECT EmpName FROM imdatabase.employee WHERE EmpName LIKE 'A%N'

# # display the record of those in 'OPN', SAL' and 'FIN' department sorted by department code in ascending order and salary in descending order
#  SELECT * FROM imdatabase.employee WHERE DeptCode IN ('OPN','SAL','FIN') ORDER BY DeptCode ASC, Salary DESC