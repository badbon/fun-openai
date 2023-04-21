
# A fictional historical person short biography generator, education, background, rise to power
# it will be split in event-based content, and biography based. Difference with event based is that it will have exact dates to attribute to, and can intertvene with other characters.
# Any non-event content therefore will be mostly situational and cosmetical more or less.
#
# UPDATE: Currently working making this universal, so it can be used for any character, not just rulers.

import random
import location_util

# Variables
title_list = ['', 'Commoner ', '', '', 'Baron ']
start_list = ["born"]

# Character traits 

strength = -1
intelligence = -1

isRich = False
isGenius = False

isRuler = True



# Gender handling (with help of pronouns)
if random.choice([True, False]):
    pronoun = "He"
else:
    pronoun = "She"

# Lists
names_list = ["John", "Adam", "Turkus", "Heinz", "David", "Alexos", "Claudia", "Megan", "Mathias", "Matward", "Gustavo", "Andre", "Andreas", "Ari", "Ariele", "Dofuso", "Viktorin"]
educations_list = ["Church of Hard Knocks", "Vales", "Candybridge", "Oxborga", "Brown", "Federal University of Amogus", "Green Military Academy"]
background_list = ["aristocrat", "noble", "royal", "patrician", "merchant", "commoner", "poor painters"]
rise_list = [" marrying the Noble of Oonga Boonga", 
             " taking the throne after their father's passing", " inheriting a large fortune",
             " giving a highly popular speech to public", " violently overthrowing his rivals and gaining full authority over his subjects"]

# Generating a Random Title
title = random.choice(title_list)

# Generating a Random Name
name = random.choice(names_list)

# Generating a Random start
start = random.choice(start_list)

# Generating a Random Education
education = random.choice(educations_list)

# Generating a Random Background
background = random.choice(background_list)

# Generating a Random Rise
rise = random.choice(rise_list)

def monster_encounter():
    monster_list = ["ancient red dragon", "black dragon", "mindflayer", "giant spider", "orc captain", 
    "beholder", "lich", "green dragon", "lich queen", "sea serpent", "hydra", "mummy" "white bear", "giant eagle", "giant scorpion", "Obus, Prince of Misfortune and Whining"]
    monster = random.choice(monster_list)
    verbs_list = ["dueled", "fought", "defeated", "confronted", "banished", "vanquished"]
    verb = random.choice(verbs_list)

    return pronoun + " encountered a " + monster + " and " + verb + " it."

def politics_encounter():
    politics_list = ["assassination", "a military coup", "a civil war", "a rebellion", "a coup d'etat", "popular revolt", "a peasant uprising", "a peasant revolt", "a peasant rebellion",
     "holy war for long oppressed wizards rights"]
    
    politicsActivity = random.choice(politics_list)
    return pronoun + " was involved in a " + politicsActivity + "."

def declaration_of_war():
    # Lists
    diplomatic_activity_list = [pronoun + " created a military alliance", pronoun + " held diplomatic talks with allies for assistance", pronoun + " aligned with powerful allies", pronoun + " extended the sphere of influence in the region"]
    war_declaration_list = ["a public declaration of war was made", "the enemy forces were outmaneouvred and routed",
     "access to essential resources were blocked", "the resources for war were hard to come by, both sides gave into attrition", "the enemy was utterly defeated in a decisive battle",
      "the enemy was rendered weak and defeated in a decisive battle", "the enemy was finally defeated in a decisive battle"]
    
    # Generating a Random diplomatic activity/war
    diplomatic_activity = random.choice(diplomatic_activity_list)
    war_declaration = random.choice(war_declaration_list)

    print("In response to a threat, {} and {}.".format(diplomatic_activity, war_declaration))


def war_started():
    progress_list = ["quickly progressed", "escalated to a large-scale war",  "progressed slowly", "remained a localised conflict", "was a long and bloody war"]
    process_list = ["with more than one enemies attacking", "over a land dispute", "for control of a important dungeon", "over a dynastic dispute"]
    outcome_list = ["as enemies were defeated", "after a treaty was signed", "as no definitive victor emerged", "in a stalemate",
     "with both sides contradicting each other and claiming total victory over their enemy"]

    progress = random.choice(progress_list)
    process = random.choice(process_list)
    outcome = random.choice(outcome_list)

    print("The war {} {} and ended {}.".format(progress, process, outcome))



def wealth_power():
    wealth_list = ["control of vast resources and land", "command of immense fleets and armies", "leadership of powerful alliances",
    "enormous wealth and influence", "forbidden knowledge of raising the dead", "gain immense respect of its army warriors and inspiration for ages to come for " + pronoun + " bravery", "control of a powerful magical artifact",
     "praise for " + pronoun + " garden of mighty statues of the grand wizards", "control of a powerful court of wizards who developed powerful magic artifacts and weaponry"]
    wealth = random.choice(wealth_list)

def lost_wealth(): 
    lost_wealth_list = ["rumours spread that " + pronoun + " was secretly a devil worshipper", "a plague ravaged the land", 
    "tensions with powerful alleis caused them to turn against their former ally", "famine"]

    return random.choice(lost_wealth_list)


def death_story(): 
    # Lists of deaths based on their status, possibilities stack up. Commoner with no wealth or power will have a less different death possibilities added on than a noble with wealth and power... lol
    death_list = ["slain in a duel against a powerful rival", "succumbing to a long illness", "killed in a hunting accident", "assassinated by their own bodyguards",
    "killed due to overexertion in battle",
     "slain in a foreign land with unknown poison", "died in a mysterious accident", "blown up by an explosions wizard", "slain by ninjas in a dark alley", "killed in an unfortunate accident with fully loaded cart full of trade goods rolling into them" ]
    # If they are a noble, they have a higher chance of dying in an assassination, political or military coup, etc. 
    ruler_death_list = ["killed in a military rebellion from their generals", "killed in a political assassination",
                        "killed in a military coup", "killed in a peasant uprising",
                        "killed in a peasant revolt", "killed in a peasant rebellion", "killed in a holy war for long oppressed wizards rights", "killed in a peasant uprising", "killed in a peasant revolt",
                        "killed in a fierce peasant rebellion", "killed in a holy war for long oppressed wizards rights", "killed by the working class in failed attempt to seize means of precious gem production"]
    if(isRuler):
        death = random.choice(ruler_death_list)
    if(isRuler == False):
        death = random.choice(death_list)
    print("In the end, " + pronoun.lower() + " was " + death + ".")

# Function to Generate range dates after "in the year XXX" for use in above events
def create_date(currentStartYear, rangeEnd):
    years_range = range(currentStartYear, rangeEnd)
    return f"In the year {random.choice(years_range)}"


#Call the functions
# Generating a Short Biography
print(create_date(1001, 1029))
birthDate = create_date(1001, 1029)
print(title + "" + name + " was " + start + " into a " + background + " family " + "and received education at " + education + ". ")
if(isRuler):
    print(pronoun + " rose to power by" + rise + ".")
    war_started()
    declaration_of_war()
    wealth_power()
print(monster_encounter())
death_story()
