import openai
import random
import util

openai.api_key = util.get_api_key()

# Pay attention if this is 002 or 003. 003 is a tiny bit more powerful. But 002 is way faster, especially when testing its great.
model_engine = "text-davinci-003"

# Base class representing a Kingdom
class Kingdom:
    def __init__(self, name, motivation, biography):
        self.name = name
        self.motivation = motivation
        self.biography = ""

    def generate_name(self):
        first_name_word = ["Aelar", "Aldair", "Alden", "Althea", "Amaranth",
                           "Amaryllis", "Amethyst", "Aneira", "Aneirin", "Arael", "Arcadia",
                           "Arcturus", "Ariadne", "Arianrhod", "Astrid",
                           "Atara", "Aurora", "Avalon", "Aviana", "Axel", "Azura",
                           "Gaeloria", "Narundor", "Draconia", "Celestria", "Silvershade", "Shadowkeep",
                           "Amberwind",
                           "Elvandar", "Wintershield", "Stormhold", "Firewatch", "Mistwood", "Wildewood", "Emberfall",
                           "Frostfang", "Ironhelm",
                           "Hollowkeep", "Goldencrest", "Crimsonreach", "Dragonfire", "Starfall", "Crystalia",
                           "Mosswood", "Rainbowrise",
                           "Thunderhold", "Gloomhaven", "Darkmoor", "Moonshadow", "Vinehaven"]
        
        last_name_word = ["Khanate", "Empire", "Duchy", "Grounds", "Lands", "Kingdom", "Realm", "Nation", "Dominion",
                          "Commonwealth", "Federation", "Republic", "Nation", "Principality", "Protectorate"]

        first_name = random.choice(first_name_word)
        last_name = random.choice(last_name_word)
        return f"{first_name} {last_name}"

    def generate_biography(self):
        custom_prompt = "Create a fantasy RPG Kingdoms objective introduction that rules in a fictional world. " \
                        "Briefly describing their philosophy, rulership, and strength as a nation. " \
                        "Their primary motivations are: " + self.motivation + " the Kingdom is named: " + self.name + \
                        "\n  (medieval, fantasy setting)"

        basic_response = openai.Completion.create(
            engine=model_engine,
            prompt=custom_prompt,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=1.0,
            timeout=20,)

        self.biography = basic_response.choices[0].text

def create_kingdom():
    races = ["Human", "Dwarf", "Elf"]
    motivations = ["glory", "riches", "power", "knowledge", "connection to the deities"]

    name = Kingdom.generate_name()
    motivation = random.choice(motivations)
    biography = Kingdom.generate_biography()
    kingdom = Kingdom(name, motivation, biography)

    return kingdom


# Create a kingdom, holder of the maps. But also backstory, civ, etc.
my_kingdom = create_kingdom()
print(my_kingdom.name)
print(my_kingdom.motivation)
print(my_kingdom.biography)
