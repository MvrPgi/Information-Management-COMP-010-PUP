import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() 

sql ="SELECT *FROM customers ORDER BY name DESC"  # Select all records from the "customers" table, and display the result starting from the highest name

mycursor.execute(sql) # execute the SQL query

myresult = mycursor.fetchall() # fetchall() method, which fetches all rows from the last executed statement

for result in myresult:
  print(result) # print all rows