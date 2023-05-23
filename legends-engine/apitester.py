import requests
import json
import util
import openai

url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
openai.api_key = util.get_api_key()
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

data = {
    "prompt": "Hello, world!",
    "max_tokens": 10,
    "n": 1,
    "stop": None,
    "temperature": 0.5,
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
