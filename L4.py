import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() method
#sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'" # Update the address from "Valley 345" to "Canyon 123"


mycursor.execute("SELECT * FROM customers LIMIT 5") # Select the first 5 records in the "customers" table

myresult = mycursor.fetchall() # fetchall() method, which fetches all rows from the last executed statement

for result in myresult:
  print(result) # print all rows

#mycursor.execute(sql) # execute the SQL query
#mydb.commit() # Commit is required to make the changes, otherwise no changes are made to the table.