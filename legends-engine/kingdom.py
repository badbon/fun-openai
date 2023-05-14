import openai
import random

openai.api_key = "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"

# Pay attention if this is 002 or 003. 003 is a tiny bit more powerful. But 002 is way faster, especially when testing its great.
model_engine = "text-davinci-003"

# Base class representing a Kingdom
class Kingdom:
    def __init__(self, name, motivation):
        self.name = name
        self.motivation = motivation
        self.biography = ""

    def generate_name(self):
        first_name_word = ["Aelar", "Aislinn", "Aldair", "Alden", "Althea", "Amaranth",
                           "Amaryllis", "Amethyst", "Anastaria", "Aneira", "Aneirin", "Arael", "Araminta", "Arcadia",
                           "Arcturus", "Ariadne", "Arianrhod", "Aristaeus", "Aristeia", "Artemis", "Astrid", "Atalanta",
                           "Atara", "Aurora", "Avalon", "Aviana", "Axel", "Azura",
                           "Gaeloria", "Aurindor", "Narundor", "Draconia", "Celestria", "Silvershade", "Shadowkeep",
                           "Amberwind",
                           "Elvandar", "Wintershield", "Stormhold", "Firewatch", "Mistwood", "Wildewood", "Emberfall",
                           "Frostfang", "Ironhelm",
                           "Hollowkeep", "Goldencrest", "Crimsonreach", "Dragonfire", "Starfall", "Crystalia",
                           "Mosswood", "Rainbowrise",
                           "Thunderhold", "Gloomhaven", "Darkmoor", "Moonshadow", "Vinehaven"]
        
        last_name_word = ["Khanate", "Empire", "Duchy", "Grounds", "Lands", "Kingdom", "Realm", "Nation", "Dominion",
                          "Commonwealth", "Federation", "Republic", "Nation", "Principality", "Protectorate", "Settlement"]

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
            timeout=20,
            )

        self.biography = basic_response.choices[0].text


# Derived class representing a Map
class Map(Kingdom):
    def __init__(self, name, motivation):
        super().__init__(name, motivation)

    def generate_map(self):
        # Logic to generate the map
        pass


def create_kingdom():
    races = ["Human", "Dwarf", "Elf"]
    motivations = ["glory", "riches", "power", "knowledge", "connection to (fictional) deities"]

    name = random.choice(races)
    motivation = random.choice(motivations)

    kingdom = Map(name, motivation)
    kingdom.generate_map()  # Call the specific method for generating the map
    return kingdom


# Create a kingdom, holder of the maps. But also backstory, civ, etc.
my_kingdom = create_kingdom()
print(my_kingdom.name)
print(my_kingdom.motivation)
print(my_kingdom.biography)
