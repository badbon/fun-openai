import mysql.connector
import os
import sys
from character import create_character
import kingdom as kingdom_gen

def insert_character(mydb):
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
    mydb.commit()
  except mysql.connector.Error as error:
    print("\nMySQL Query Error:", error)
  finally:
    cursor.close()

def insert_kingdom(mydb):
  kingdom = kingdom_gen.create_kingdom()
  
  try:
    query = """
    INSERT INTO kingdoms (name, characters_associated, biography)
    VALUES (%s, %s, %s)"""
    
    name = kingdom.name
    characters_associated = ''
    biography = kingdom.biography

    cursor = mydb.cursor()
    cursor.execute(query, (name, characters_associated, biography))
    mydb.commit()
  except mysql.connector.Error as error:
    print("\nMySQL Query Error:", error)
  finally:
    cursor.close()

def initialize_db(mydb):
  cursor = mydb.cursor()
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
  mydb.commit()
  cursor.close()

def main(num_characters, num_kingdoms):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('password.txt', 'r') as file:
        fileReadPassword = file.read().strip()
    mydb = mysql.connector.connect(
        host="localhost",
        user="dungeon",
        password=fileReadPassword,
        database="rkdb"
    )
    initialize_db(mydb)
    for _ in range(num_characters):
        insert_character(mydb)
    for _ in range(num_kingdoms):
        insert_kingdom(mydb)
    mydb.close()

# Run this file with the number of characters and kingdoms to generate
if __name__ == "__main__":
    # Check for correct number of arguments, warn/exit if incorrect
    if len(sys.argv) != 3:
        print("Please provide the number of characters and kingdoms to generate.")
        sys.exit(1)
    num_characters = int(sys.argv[1])
    num_kingdoms = int(sys.argv[2])
    main(num_characters, num_kingdoms)