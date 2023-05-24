import mysql.connector
import os
from character import create_character
import kingdom as kingdom_gen

# Change the working directory to the location of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create a file called password.txt and store your MySQL password in it (gitignore will ignore this file)
with open('password.txt', 'r') as file:
    fileReadPassword = file.read().strip()

mydb = mysql.connector.connect(
  host="localhost",
  user="dungeon",
  password=fileReadPassword,
  database="rkdb"
)

# CHARACTER TABLE
def insert_character():
  character = create_character()
  cursor = mydb.cursor()
  try:
    query = """
    INSERT INTO characters (full_name, kingdom, race, biography, motivation, intent, history)
    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    full_name = character['full_name']
    kingdom = character['kingdom']
    race = character['race']
    biography = character['biography']
    motivation = character['motivation']
    intent = character['intent']
    history = character['history']

    cursor.execute(query, (full_name, kingdom, race, biography, motivation, intent, history))
    # Commit the changes to the database
    mydb.commit()

  except mysql.connector.Error as error:
    print("\nMySQL Query Error:", error)

  finally:
    # Close the connection
    cursor.close()
    mydb.close()

def insert_kingdom():
  kingdom = kingdom_gen.create_kingdom()
  
  try:
    query = """
    INSERT INTO kingdoms (name, characters_associated, biography)
    VALUES (%s, %s, %s)"""
    
    name = kingdom.name
    characters_associated = ''
    biography = kingdom.biography

    cursor = mydb.cursor()
    print("\nDB: " + str(mydb))
    cursor.execute(query, (name, characters_associated, biography))
    mydb.commit()
  
  except mysql.connector.Error as error:
    print("\nMySQL Query Error:", error)
    
  finally:
    cursor.close()
    mydb.close()


# -----
# Useful for first run on localhost
def initialize_db():
  # Create a cursor object to execute SQL queries
  cursor = mydb.cursor()

  # Create table - characters
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS characters (
      id INT AUTO_INCREMENT PRIMARY KEY,
      full_name VARCHAR(255),
      kingdom VARCHAR(255),
      race VARCHAR(255),
      biography TEXT,
      motivation TEXT,
      intent TEXT,
      history TEXT)""")

  # Create table - kingdoms
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS kingdoms (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255),
      characters_associated VARCHAR(255),
      biography TEXT)""")
  
  cursor.execute("""CREATE TABLE IF NOT EXISTS maps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roombased TINYINT,
    population TINYINT,
    wealth TINYINT,
    civilized TINYINT,
    name VARCHAR(255),
    intro TEXT,
    history TEXT);""")


  # Commit the changes and close the connection
  mydb.commit()
  cursor.close()
  mydb.close()
  
  
# initialize_db()
insert_kingdom()
#insert_character()