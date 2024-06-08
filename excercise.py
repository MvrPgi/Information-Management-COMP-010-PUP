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






############################################################################################################

# Data to be inserted into the student table
# data_to_insert = [
#     ('2016-123', 'Kenra', 'Lee', 'A', 'BSCS', 'IR', '0921-9999', '#14 Flower St., Sampaloc Manila', '2016-6-1', 1.25, 300),
#     ('2017-321', 'Sophia', 'Dy', 'G', 'BSCS', 'IR', '0933-1111', 'Blk1 Lot 4 Ingels Ave. Pasig City', '2017-6-1', 3, 20),
#     ('2018-222', 'James', 'Cuevas', 'H', 'BSIT', 'R', '0917-1234', '45 Hiligaynon St., Quezon City', '2018-6-1', 2.75, 5),
#     ('2019-223', 'Jett', 'Li', 'T', 'BSIT', 'R', '0918-4321', '#66 Wakas St, Q.C.', '2019-6-1', 1.25, 0),
#     ('2019-123', 'Pauline', 'Go', 'Y', 'BSCE', 'R', '0999-9999', '89 Silver Ave. Manila', '2019-6-1', 1, 10),
#     ('2018-122', 'Thea', 'Reyes', 'B', 'BSIT', 'R', '0939-9090', '78 Sure St., Tondo, Manila', '2018-6-1', 1.5, 0),
#     ('2019-224', 'Eunise', 'Sy', 'D', 'BSCS', 'R', '0977-1122', '111 Anonas St, Sta. Mesa, Manila', '2019-6-1', 1.75, 50),
#     ('2017-999', 'Nats', 'Diaz', 'C', 'BSCE', 'IR', '0933-3434', '90 Taal St, La Loma, Q.C.', '2017-6-1', 2, 10),
#     ('2018-555', 'Janice', 'Co', 'V', 'BSME', 'R', '0915-5555', 'Blk 53 Lot 35 Greenbreeze St, Q.C.', '2018-6-1', 2, 10),
#     ('2016-298', 'Genie', 'Lopez', 'R', 'BSEE', 'IR', '0919-7777', '#123 Anywhere Ave., Pasig', '2016-6-1', 1.25, 0),
#     ('2021-300', 'Lydia', 'Vega', 'R', 'BSCS', 'R', '0919-7897', '#56 Honesty St., Pasay', '2021-6-1', 1.25, 20)
# ]

# # SQL query for inserting data
# insert_query = """
# INSERT INTO student (StudID, FirstName, LastName, MidInit, Program, Status, ContactNum, Address, DateAdmitted, GWA, TuitionBalance) 
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """

# # Executing the query with the data
# try:
#     mycursor.executemany(insert_query, data_to_insert)
#     mydb.commit()  # Commit your changes in the database
#     print(f"{mycursor.rowcount} records inserted successfully.")
# except Exception as e:
#     mydb.rollback()  # Rollback in case of any error
#     print(f"Failed to insert records into student table. Error: {e}")


# NO 4
# SELECT * FROM imdatabase.student 
# WHERE Program IN ('BSCS', 'BSIT') 
# AND GWA >= 1.25;  

# SELECT * FROM imdatabase.student
# WHERE Program NOT IN('BSCS', 'BSIT') 
# AND GWA >= 1.5;

# SELECT * FROM imdatabase.student 
# WHERE Address LIKE '%Manila%' 
# AND GWA >= 1.75;


# SELECT * FROM imdatabase.student 
# WHERE (Program IN ('BSCS', 'BSIT') AND GWA <= 1.25)
# OR (Program NOT IN('BSCS', 'BSIT') AND GWA <= 1.5)
# OR (Address LIKE '%Manila%' AND GWA <= 1.75);





# SELECT division, job AVG(salary)
# FROM basetable
# WHERE position LIKE 'RF'
# GROUP BY div, job
# HAVING AVG(salary) > 30000
# ORDER BY average_salary;



