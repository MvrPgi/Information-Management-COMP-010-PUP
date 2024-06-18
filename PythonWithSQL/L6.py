import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() 

sql = "DELETE FROM customers WHERE address = 'Canyon 123'" # Delete any record where the address is "Mountain 21"

mycursor.execute(sql) # execute the SQL query
mydb.commit() # Commit is required to make the changes, otherwise no changes are made to the table.