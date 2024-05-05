import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() method
sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'" # Update the address from "Valley 345" to "Canyon 123"

mycursor.execute(sql) # execute the SQL query
mydb.commit() # Commit is required to make the changes, otherwise no changes are made to the table.