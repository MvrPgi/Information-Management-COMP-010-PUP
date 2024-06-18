import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers") # Select all records from the "customers" table
myresult = mycursor.fetchall() # fetchall() method, which fetches all rows from the last executed statement
for row in myresult:
  print(row) # print all rows


mycursor.execute("SELECT name FROM customers") # Select only the name and address columns
myresult = mycursor.fetchall() # fetchall() method, which fetches all rows from the last executed statement
for row in myresult:
  print(row) # print all rows
