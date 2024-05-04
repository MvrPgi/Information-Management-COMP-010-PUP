import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE DB1")  # Create a database named TestDB

mycursor.execute("SHOW DATABASES")  # Show all databases

for db in mycursor:
  print(db)  # Print all databases