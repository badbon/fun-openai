import openai
import os
import random
import string

openai.api_key = "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"
model_engine = "text-davinci-002"

def generate_name():
    """Generate a random fantasy character name."""
    first_names = ["Aelar", "Aerin", "Aeron", "Aiden", "Aila", "Ailis", "Aislinn", "Alaric", "Aldair", "Alden", "Althaea", "Althea", "Amaranth", "Amaryllis", "Amethyst", "Anastaria", "Andriel", "Aneira", "Aneirin", "Arael", "Araminta", "Arcadia", "Arcturus", "Ariadne", "Arianrhod", "Arien", "Arin", "Arista", "Aristaeus", "Aristeia", "Artemis", "Arya", "Asphodel", "Astrid", "Atalanta", "Atara", "Aurora", "Avalon", "Aviana", "Axel", "Ayla", "Azura"]
    last_names = ["Ashworth", "Blackwood", "Bloodmoon", "Darkwater", "Drakon", "Dragonrider", "Elmwood", "Fairwind", "Frostfire", "Goldheart", "Goldmane", "Hartwood", "Icetongue", "Ironclaw", "Ironfoot", "Moonwhisper", "Nightshade", "Oakenshield", "Ravenwood", "Redmane", "Rosewater", "Silversmith", "Snowdrift", "Stagrunner", "Stargazer", "Starweaver", "Stormchaser", "Stormcaller", "Stormwatcher", "Sunspear", "Thornbush", "Thunderstrike", "Vale", "Waverunner", "Whitethorn", "Wildfire", "Wildheart", "Wintermoon", "Wolfbloom", "Woodland", "Wyrmslayer"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

# Define possible options for character attributes
races = ["Human", "Dwarf", "Elf"]
hair_colors = ["black", "blonde", "brown", "red", "gray"]
hair_styles = ["short", "medium", "long", "curly", "straight"]
motivations = ["glory", "revenge", "riches", "power", "knowledge"]

# Randomly select character attributes
name = generate_name()

race = random.choice(races)
hair_color = random.choice(hair_colors)
hair_style = random.choice(hair_styles)
motivation = random.choice(motivations)

def generate_word(length):
   """Generate a random word with the specified length."""
   letters = string.ascii_lowercase
   word = ''.join(random.choice(letters) for _ in range(length))
   return word


# Generate basic physical facts and personal motivations
basic_prompt = "Create a fantasy RPG character who lives in a medieval world and explores dungeons to \
    defeat skeletons and other monsters! Do not actually describe their equipment or skills, or current age. this section is more of an intro. Character Name: " + name.lower()
    
#print("Inputting an intro prompt: " + basic_prompt)
basic_response = openai.Completion.create(
    engine=model_engine,
    prompt=basic_prompt,
    max_tokens=220,
    n=1,
    stop=None,
    temperature=1.0,
    timeout=20,  
)

# OpenAI prompt
history_prompt = f"Create a medieval fantasy RPG {name} character with \
    {hair_color} {hair_style} hair. of {race.lower()} race. Describe the character's personality and motivations. What adventures has the character been on in their quest for {motivation}? \
        Generate a short story about the character. Be aware of previous intro not to make contradictions: " + basic_response.choices[0].text
        
#print("Inputting a history prompt: " + history_prompt)
history_response = openai.Completion.create(
    engine=model_engine,
    prompt=history_prompt,
    max_tokens=350,
    n=1,
    stop=None,
    temperature=1.0,
    timeout=20, 
)

# Extract information from history response
history = history_response.choices[0].text

# Extract character name and other necessary attributes

char_name = name
char_motivations = motivation

# Print final results
print(basic_response.choices[0].text)
print("\n" + history_response.choices[0].text)
def debug():
    print("Character name: " + char_name)
    print("Character motivations: " + char_motivations)
debug()