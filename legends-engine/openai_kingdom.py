import openai
import random
import string

openai.api_key = "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"

# Pay attention if this is 002 or 003. 003 is a tiny bit more powerful. But 002 is way faster, especially when testing its great.
model_engine = "text-davinci-003" 


# Kingdom Name Generator
def generate_name():
    first_name_word = ["Aelar", "Aerin", "Aeron", "Aiden", "Aislinn", "Aldair", "Alden", "Althea", "Amaranth", "Amaryllis", "Amethyst", "Anastaria", "Aneira", "Aneirin", "Arael", "Araminta", "Arcadia", \
                       "Arcturus", "Ariadne", "Arianrhod", "Aristaeus", "Aristeia", "Artemis", "Astrid", "Atalanta", "Atara", "Aurora", "Avalon", "Aviana", "Axel", "Azura" \
                            "Gaeloria",    "Aurindor",    "Narundor",    "Draconia",    "Celestria",    "Silvershade",    "Shadowkeep",    "Amberwind", \
                            "Elvandar",   "Wintershield",    "Stormhold",    "Firewatch",    "Mistwood",    "Wildewood",    "Emberfall",    "Frostfang",    "Ironhelm",  \
                            "Hollowkeep",    "Goldencrest",    "Crimsonreach",    "Dragonfire",    "Starfall",   "Crystalia",    "Mosswood",    "Rainbowrise",   
                            "Thunderhold",    "Gloomhaven",    "Darkmoor",    "Moonshadow",    "Skyhaven"]
    last_name_word = ["Khanate", "Empire", "Duchy", "Grounds", "Lands", "Kingdom", "Realm", "Nation", "Dominion", "Commonwealth", "Federation", "Republic", "Nation", "Principality", "Protectorate", "Settlement"]

    first_name = random.choice(first_name_word)
    last_name = random.choice(last_name_word)
    return f"{first_name} {last_name}"

# Define possible options for character attributes
races = ["Human", "Dwarf", "Elf"]

motivations = ["glory", "riches", "power", "knowledge", "connection to (fictional) dieties"]
#prompt_clarification = "Do not actually describe their equipment, or current age. this section is more of an intro and short biography. Character Name: "

# Randomly select Kingdom attributes
name = generate_name()
race = random.choice(races)
motivation = random.choice(motivations)
 
# More customized prompts testing
custom_prompt = "Create a fantasy RPG Kingdoms objective introduction that rules in a fictional world. Briefly describing their philosophy, rulership and strength as a nation. Their primary motivations are: " + motivation + " the Kingdom is named: " + name + "\n  (medieval, fantasy setting)"

# OpenAI prompt
basic_response = openai.Completion.create(
    engine=model_engine,
    prompt=custom_prompt,
    max_tokens=300,
    n=1,
    stop=None,
    temperature=1.0,
    timeout=20,  
)


def debug():
    print("name: " + name)
    print("motivations: " + motivation)

# Print final results
debug()

print("Response: \n " + basic_response.choices[0].text)