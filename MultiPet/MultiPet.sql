USE alwyndb;
set sql_safe_updates = 0;
UPDATE alwyndb.multipet
SET Age = Floor(DATEDIFF(CURDATE(), Birthdate)/365.25);
SET SQL_SAFE_UPDATE =1;


SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

-- Number 1 Display the name of the pets and the number of visits to the vet.  Include in the list only those who had visited the vet just once. 
SELECT PetName,COUNT(PetName) As NumberOfVisit
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d
WHERE p.PetID = d.PetID
GROUP BY PetName
HAVING NumberOfVisit = 1;


-- Number 2 Display the name of the owner and the number of pets owned. 
-- Display The Name Of The Owner And The Number Of Pets Owned
SELECT * FROM alwyndb.multiowner;
SELECT * FROM alwyndb.multipet;

SELECT OwnerName, COUNT(PetName) As NumberOfPets
FROM alwyndb.multipet AS p , alwyndb.multiowner AS d
WHERE p.Owner = d.Owner
GROUP BY OwnerName;

-- Number 3 Display all pet information and owner name. Display only those whose owners are from Manila. Sort by age , from the oldest to the youngest. 

SELECT * FROM alwyndb.multiowner;
SELECT * FROM alwyndb.multipet;

Select *
FROM alwyndb.multipet AS p , alwyndb.multiowner AS d
WHERE (p.Owner = d.Owner)
AND(Address Like '%Manila%')
ORDER BY Age DESC;


-- Number 4 Display pet name, date of visit to the vet, and the name of procedure done during the visit. 
SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

SELECT PetName,DateofVisit, _Procedure
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d
WHERE p.PetID = d.PetID;

-- Number 5 Display the total amount paid to the vet for all the procedures done to the pet.  Include also the name of the pet
SELECT * FROM alwyndb.multiprocedure;
SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

SELECT PetName, SUM(fee) As TotalAmount
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d, alwyndb.multiprocedure AS m
WHERE p.PetID = d.PetID AND d._Procedure = m.ProcCode
GROUP BY PetName;

-- Number 6 List the names and age of the  pets which have been spayed or neutered  
SELECT * FROM alwyndb.multiprocedure;
SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

SELECT PetName, _Procedure
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d, alwyndb.multiprocedure AS m
WHERE p.PetID = d.PetID AND d._Procedure = m.ProcCode
AND _PROCEDURE IN ('NEU','SPY')
GROUP BY PetName, _Procedure;



-- Number 7 List the name pets which   already have their rabies vaccination  for the current year 
SELECT * FROM alwyndb.multiprocedure;
SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

SELECT PetName, _Procedure
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d, alwyndb.multiprocedure as m
WHERE (p.PetID = d.PetID) AND (d._Procedure = m.ProcCode)
	AND ProcCode = 'RAV'
	AND YEAR(DateofVisit) = "2024";



-- Number 8 Display the name of the  pets which have been vaccinated twice for rabies 

SELECT * FROM alwyndb.multiprocedure;
SELECT * FROM alwyndb.doctorvisit;
SELECT * FROM alwyndb.multipet;

SELECT PetName, COUNT(_Procedure) AS VaccinationCount
FROM alwyndb.multipet AS p , alwyndb.doctorvisit AS d, alwyndb.multiprocedure as m
WHERE (p.PetID = d.PetID) AND (d._Procedure = m.ProcCode)
	AND ProcCode ='RAV'
GROUP BY PetName, _Procedure
HAVING VaccinationCount = 2;

