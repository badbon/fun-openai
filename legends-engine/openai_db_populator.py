import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="rkdb"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Insert data into the Characters table
sql = "INSERT INTO Characters (name, age, gender) VALUES (%s, %s, %s)"
val = ("John", 32, "Male")
mycursor.execute(sql, val)
mydb.commit()

# Insert data into the Kingdoms table
sql = "INSERT INTO Kingdoms (name, population, ruler) VALUES (%s, %s, %s)"
val = ("Asgard", 1000000, "Odin")
mycursor.execute(sql, val)
mydb.commit()

# Close the database connection
mydb.close()
