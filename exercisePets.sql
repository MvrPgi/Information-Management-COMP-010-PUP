
USE imdatabase

SELECT * FROM imdatabase.pet;

-- 1. Compute the age of all the pets and update the Age attribute with the computed age.
UPDATE imdatabase.pet
SET Age = TIMESTAMPDIFF(YEAR, STR_TO_DATE(BirthDate, '%d/%m/%Y'), CURDATE());
set sql_safe_updates = 0;
 
-- 2. Display the average weight of each breed per pet type.  Display in ascending order of the pet type and breed and descending order of the average weight 

SELECT Breed, PetType, ROUND(AVG(weight), 2) AS average_weight
FROM imdatabase.pet
GROUP BY Breed, PetType
ORDER BY PetType ASC, Breed ASC, average_weight DESC;


-- 3. Display the names of all female cats, with their breed if the age is less than 2 yrs old.  Display also the name and breed of all female dogs if their age is greater than 3 yrs old.  Sort by pet type, in ascending order of the name. 
SELECT PetName, Breed
FROM imdatabase.pet
WHERE (PetType = 'cat' AND Sex = 'F' AND Age < 2)
   OR (PetType = 'dog' AND Sex = 'F' AND Age > 3)
ORDER BY PetType ASC, PetName ASC;

-- 4. Display the names, breed of pets whose color  has  ‘white’  which are owned by owners with a ‘DB’ in the owner code. 
SELECT PetName, Breed
FROM imdatabase.pet
WHERE FurColor LIKE '%white%'
AND Owner LIKE '%DB%';


--  5. Display the count per pet type and breed. Sort by pet type and breed
SELECT PetType, Breed, COUNT(*) AS PetCount
FROM imdatabase.pet
GROUP BY PetType, Breed
ORDER BY PetType, Breed;

-- 6. Display the pet owner and the count of pets he owns.  Count only the pets who are less than 2 yrs old.  Display from those who own the most number of pets.
SELECT Owner, COUNT(PetName) AS number_of_pets
FROM imdatabase.pet
WHERE Age < 2
GROUP BY Owner
ORDER BY number_of_pets DESC; 

-- 7 Display all records for those who weigh 3 kilos or more .. Display by pet type, breed, age, all in ascending order. 
SELECT PetType, Breed, Age
FROM imdatabase.pet
WHERE Weight >= 3
ORDER BY PetType ASC, Breed ASC, Age ASC; 

-- 8 Display the average weight for all breeds which are 1 to 3 yrs old and display only the averages which are greater than 3 
SELECT Breed, ROUND(AVG(Weight), 2) AS average_weight
FROM imdatabase.pet
WHERE Age BETWEEN 1 AND 3
GROUP BY Breed
HAVING average_weight > 3;



-- 9 How many dogs were born during the summer months, March to May? 
SELECT PetName, PetType,COUNT(*) AS summer_dogs
FROM imdatabase.pet
WHERE PetType = 'Dog'
AND EXTRACT(MONTH FROM STR_TO_DATE(BirthDate, '%d/%m/%Y')) BETWEEN 3 AND 5
GROUP BY PetName;


-- 10. Display how many dogs were born each month of the year 2020 
SELECT PetName, PetType,COUNT(*) AS DOGSMONTH
FROM imdatabase.pet
WHERE PetType = 'Dog'
AND EXTRACT(MONTH FROM STR_TO_DATE(BirthDate, '%d/%m/%Y')) BETWEEN 1 AND 12
GROUP BY PetType, PetName;
