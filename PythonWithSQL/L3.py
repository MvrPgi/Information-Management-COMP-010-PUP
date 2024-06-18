import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() method
sql = "Select * from customers where address = 'Park Lane 38'" # Select records where the address is "Park Lane 38"
mycursor.execute(sql) # execute the SQL query
myresult = mycursor.fetchall() # fetchall() method, which fetches all rows from the last executed statement
for row in myresult:
  print(row) # print all rows