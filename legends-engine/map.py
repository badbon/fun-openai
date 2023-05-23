import openai
from textblob import TextBlob
import util

openai.api_key = util.get_api_key()

room_options = ['Very Tunnely', 'Slightly Tunnely', 'Neutral', 'Slightly Roomy', 'Very Roomy']
pop_options = ['Very Low Pop', 'Low Pop', 'Neutral', 'High Pop', 'Very High Pop']
wealth_options = ['Very Poor', 'Poor', 'Neutral', 'Rich', 'Very Rich']
civilization_options = ['Barren', 'Low Civ', 'Neutral', 'High Civ', 'Very High Civ']

room = room_options[4]
pop = pop_options[1]
wealth = wealth_options[2]
civilization = civilization_options[0]
print(room)
print(pop)
print(wealth)
print(civilization)