import openai
import util
import random

OPENAI_API_KEY = util.get_api_key()
MODEL_ENGINE = "text-davinci-002"
MODEL_ENGINE_BTEST = "text-davinci-003"

def generate_random_attribute(attribute_list):
    return random.choice(attribute_list)

def generate_name():
    first_names = ["Aelar", "Aerin", "Aeron", "Aiden", "Aila", "Ailis", "Aislinn", "Alaric", "Aldair", "Alden", "Althaea", "Althea", "Amaranth", "Amaryllis", "Amethyst", "Anastaria", "Andriel", "Aneira", "Aneirin", "Arael", "Araminta", "Arcadia",
                   "Arcturus", "Azura"]
    
    last_names = ["Ashworth", "Blackwood", "Bloodmoon", "Darkwater", "Drakon", "Dragonrider", "Elmwood", "Fairwind", "Frostfire", "Goldheart", "Goldmane", "Hartwood", "Icetongue", "Ironclaw", "Ironfoot", "Moonwhisper", "Nightshade", "Oakenshield",
                  "Ravenwood", "Redmane", "Rosewater", "Silversmith", "Snowdrift", "Stagrunner", "Stargazer", "Starweaver", "Stormchaser", "Stormcaller", "Stormwatcher", "Sunspear", "Thornbush", "Thunderstrike", "Vale", "Waverunner", "Whitethorn",
                  "Wildfire", "Wildheart", "Wintermoon", "Wolfbloom", "Woodland", "Wyrmslayer"]

    first_name = generate_random_attribute(first_names)
    last_name = generate_random_attribute(last_names)
    return f"{first_name} {last_name}"

def create_character():
    # Define possible options for character attributes
    races = ["Human", "Dwarf", "Elf"]
    motivations = ["glory", "seeking life meaning", "riches", "power", "knowledge"]

    types_of_character_intent = ["trade and converse with adventurers! ", "find a new adventurer to lead him to battle and glory.", "defeat skeletons and other monsters!", "get very rich exploring and gathering ores and gems in dangerous dungeons" ]
    prompt_clarification = "Do not actually describe their equipment, or current age. this section is more of an intro and short biography. Character Name: "

    # Randomly select character attributes
    name = generate_name()

    race = generate_random_attribute(races)
    motivation = generate_random_attribute(motivations)
    intent = generate_random_attribute(types_of_character_intent)
    
    # More customized prompts testing
    custom_prompt = f"Create a fantasy RPG character who lives in a medieval fictional world and currently lives in the dungeons to {intent}{prompt_clarification}{name.lower()}"

    try:
        # OpenAI prompt
        basic_response = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=custom_prompt,
            max_tokens=180,
            n=1,
            stop=None,
            temperature=1.0,
            timeout=20,  
        )
    except openai.error.OpenAIError as e:
        print(f"Received error from OpenAI: {e}")
        return None

    history_prompt = f"Create a medieval fantasy RPG {name} character with of {race.lower()} race. Describe the character's personality and motivations. What adventures has the character been on in their quest for {motivation}? Generate a short adventures story about the character. Be aware of preceeding intro not to make contradictions: {basic_response.choices[0].text}"
    print("DEBUG: " + history_prompt)

    try:  
        history_response = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=history_prompt,
            max_tokens=240,
            n=1,
            stop=None,
            temperature=1.0,
            timeout=20, 
        )
    except openai.error.OpenAIError as e:
        print(f"Received error from OpenAI: {e}")
        return None

    # Extract information from history response
    history = history_response.choices[0].text

    # Extract character name and other necessary attributes

    char_name = name
    char_motivations = motivation

    character = {
        'full_name': char_name,
        'kingdom': 'Kingdom',
        'race': race,
        'motivation': char_motivations,
        'intent': intent,        
        'biography': basic_response.choices[0].text,
        'history': history_response.choices[0].text,
    }
    return character