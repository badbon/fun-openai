import mysql.connector
import os
import openai_character
from openai_character import create_character

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

def insert_character():
  character = create_character()
  

  query = """
  INSERT INTO characters (full_name, kingdom, race, biography, motivation, intent, history)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
  """
  
  full_name = character['full_name']
  kingdom = character['kingdom']
  race = character['race']
  biography = character['biography']
  motivation = character['motivation']
  intent = character['intent']
  history = character['history']

  cursor = mydb.cursor()
  cursor.execute(query, (full_name, kingdom, race, biography, motivation, intent, history))
  mydb.commit()
  cursor.close()
  mydb.close()


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