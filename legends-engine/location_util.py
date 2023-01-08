# Mostly used for debugging. When there is no real locations generated, we will have to rely on random temporary strings.
import random

def print_dummy_kingdom():
    kingdom_names = ["Fighters of Agony", "Southside Kings Union", "Seabottom", "Oonga Boonga"]
    return random.choice(kingdom_names)

def print_dummy_location():
   names = ["Nice Castle Co.", "Bricked Tavern", "Fair Pub", "Fine Tower of Fun", "Wojakson Tavern"]
   return random.choice(names)