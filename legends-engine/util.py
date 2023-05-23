def get_api_key():
# You need to create a file called apikey.txt and store your Openai API key in it (gitignore will ignore this file)
   with open('apikey.txt', 'r') as file:
      fileRead = file.read().strip()
      return fileRead