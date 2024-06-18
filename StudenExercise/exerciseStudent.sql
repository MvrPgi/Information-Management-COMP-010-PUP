USE imdatabase;
SELECT * FROM imdatabase.student;

-- list the lastname, program, and gwa of BSIT BSCS student whose gwa is 1 -1.75 sort by desc
SELECT LastName,GWA, Program
FROM student
WHERE Program IN('BSIT','BSCS')
	AND GWA BETWEEN 1 AND 1.75
ORDER BY GWA DESC;

-- Select all records which satisfy any of the 2 combinations of conditions below:
-- 2.1 GWA is 1, 1.25 , or 1.5 and student lives in Manila
-- 2.2 GWA is 1, 1.25 , or 1.5 or 1.75 and student lives outside of Manila

SELECT StudID, GWA, Address
FROM student
WHERE
Address LIKE '%Manila%'
        AND GWA BETWEEN 1 AND 1.5
        OR GWA BETWEEN 1 AND 1.75;


-- Display the student id, last name, program , status, date admitted for those which satisfy either of the following criteria 
-- status is regular and date admitted is earlier than 2019
-- status is irregular and and date admitted is 2019 and above


SELECT StudID, LastName, Program, _Status,DateAdmitted
FROM student
WHERE (_Status = 'R' AND DateAdmitted < '2019-01-01')
   OR (_Status = 'IR' AND DateAdmitted >= '2019-01-01');
   
-- Display the student records which satisfy any of the following conditions
 -- 4.1 program is IT related (CS, IT), GWA is at least 1.25
 -- 4.2 if program is non IT, GWA is at least 1.5
 -- 4.3 resident of Manila, regardless of the course, GWA is at least 1.7
 
SELECT StudID, Program, GWA, Address
FROM student
WHERE(Program IN ('CS','IT') AND GWA BETWEEN 1 AND 1.25)
OR (Program NOT IN('CS','IT')AND GWA BETWEEN 1 AND 1.5)
OR (Address LIKE '%Manila%' AND GWA BETWEEN 1 AND 1.75);
   
   