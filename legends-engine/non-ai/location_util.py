# Mostly used for debugging. When there is no real locations generated, we will have to rely on random temporary strings.
import random

def print_dummy_kingdom():
    kingdom_names = ["Fighters of Agony", "Southside Kings Union", "Seabottom", "Oonga Boonga"]
    return random.choice(kingdom_names)

def print_dummy_location(isCombined):
    # Tavern, establishment, fort
    first_words = ["Nice", "Fire", "Water", "Tea", "Brick", "Tiny", "Moon", "Bastion Of"]
    second_words = ["Consuming Hall", "Timebox", "Earthly Properties", "Magical", "Sorcering Sorcer", "Being Nice", "Forest Cutters", "Forest Guard", "Tolerable Guard", "Barely Tolerable Guard", "Disgust and Hate", "Dissapointings", "Guard"]
    names = ["Nice Castle Co.", "Bricked Tavern", "Fair Pub", "Fine Tower of Fun", "Wojakson Tavern"]
    if(isCombined):
        return random.choice(first_words) + random.choice(second_words)
    return random.choice(names)

# Function to Generate range dates after "in the year XXX" for use in above events" - originally from ruler_legends
def create_date(currentStartYear, rangeEnd, yearOnly):
    years_range = range(currentStartYear, rangeEnd)
    if (yearOnly):
        return f"{random.choice(years_range)}"
    return f"In the year {random.choice(years_range)}"

print(print_dummy_location(True))