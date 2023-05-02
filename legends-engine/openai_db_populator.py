import mysql.connector
import os

# Change the working directory to the location of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create a file called password.txt and store your MySQL password in it (gitignore will ignore this file)
with open('password.txt', 'r') as file:
    fileReadPassword = file.read().strip()

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="dungeon",
  password = fileReadPassword,
  database="rkdb"
)

def populate_db():
  cursor = mydb.cursor()
  
  cursor.execute("UPDATE")

# Useful for first run on localhost
def initialize_db():
  # Create a cursor object to execute SQL queries
  cursor = mydb.cursor()

  # Create table - characters
  cursor.execute("""
  CREATE TABLE characters (
      id INT AUTO_INCREMENT PRIMARY KEY,
      full_name VARCHAR(255),
      kingdom VARCHAR(255),
      race VARCHAR(255),
      biography TEXT,
      motivation TEXT,
      intent TEXT,
      history TEXT
  )
  """)

  # Create table - kingdoms
  cursor.execute("""
  CREATE TABLE kingdoms (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255),
      characters_associated VARCHAR(255),
      biography TEXT
  )
  """)

  # Commit the changes and close the connection
  mydb.commit()
  cursor.close()
  mydb.close()