import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase" # create database mydatabase
)


mycursor = mydb.cursor() # Create a cursor object using the cursor() method

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"   # Insert multiple rows into the customers table, with one SQL statement
customers = [("John", "Highway 21"),
             ("Peter", "Lowstreet 4"),
             ("Amy", "Apple st 652"),
             ("Hannah", "Mountain 21"),
             ("Michael", "Valley 345"),
             ("Sandy", "Ocean blvd 2"),
             ("Betty", "Green Grass 1"),
             ("Richard", "Sky st 331"),
             ("Susan", "One way 98"),
             ("Vicky", "Yellow Garden 2"),
             ("Ben", "Park Lane 38"),
             ("Justine", "Park Lane 38"),
             ("William", "Central st 954"),
             ("Chuck", "Main Road 989"),
             ("Viola", "Sideway 1633")]
mycursor.executemany(sql, customers) # executemany() method to perform multiple queries at once
mydb.commit() # commit() method to make the changes, otherwise no changes are made to the table.