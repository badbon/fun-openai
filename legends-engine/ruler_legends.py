
# A fictional historical person short biography generator, education, background, rise to power
# it will be split in event-based content, and biography based. Difference with event based is that it will have exact dates to attribute to, and can intertvene with other characters.
# Any non-event content therefore will be mostly situational and cosmetical more or less.
import random
import location_util

# Variables
title_list = ['King', 'Queen', 'Prince', 'Duke', 'Baron']
start_list = ["born"]

# Gender handling (with help of pronouns)
if random.choice([True, False]):
    pronoun = "He"
else:
    pronoun = "She"

# Lists
names_list = ["John", "Adam", "Turkus", "Heinz", "David", "Alexos", "Claudia", "Megan", "Mathias", "Matward", "Gustavo", "Andre", "Andreas", "Ari", "Ariele", "Dofuso", "Viktorin"]
educations_list = ["Church of Hard Knocks", "Vales", "Candybridge", "Oxborga", "Brown", "Federal University of Amogus", "Green Military Academy"]
background_list = ["aristocrat", "noble", "royal", "doge", "merchant", "commoner", "poor painters"]
rise_list = [" marrying the Princess of Oonga Boonga", 
             " taking the throne after their father's passing", " inheriting a large fortune",
             " giving a highly popular speech to public", "violently overthrowing his rivals and gaining full authority over his subjects"]

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
    "beholder", "lich", "green dragon", "lich queen", "sea serpent", "hydra", "mummy" "white bear", "giant eagle", "giant scorpion"]
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
    diplomatic_activity_list = [pronoun + " created a military alliance", pronoun + " held diplomatic talks with allies for assistance", pronoun + " aligned with powerful allies", pronoun + " extended the sphere of influence in the region"]
    war_declaration_list = ["a public declaration of war was made", "the enemy forces were outmaneouvred and routed",
     "access to essential resources were blocked", "the resources for war were hard to come by, both sides gave into attrition", "the enemy was utterly defeated in a decisive battle",
      "the enemy was rendered weak and defeated in a decisive battle", "the enemy was finally defeated in a decisive battle"]
    diplomatic_activity = random.choice(diplomatic_activity_list)
    war_declaration = random.choice(war_declaration_list)

    print("In response to a threat, {} and {}.".format(diplomatic_activity, war_declaration))


def war_started():
    progress_list = ["quickly progressed", "escalated to a large-scale war",  "progressed slowly", "remained a localised conflict", "was a long and bloody war"]
    process_list = ["with more than one enemies attacking", "over a land dispute", "for control of a important dungeon", "over a dynastic dispute"]
    outcome_list = ["enemies were defeated", "a treaty was signed", "no definitive victor emerged", "the war ended in a stalemate",
     "the war ended with both sides claiming total victory over their enemy"]

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
    death_list = ["slain in a duel against a powerful rival", "succumbing to a long illness", "killed in a hunting accident", 
    "killed in a political assassination", "assassinated by their own bodyguards",
    "killed due to overexertion in battle",
     "slain in a foreign land with unknown poison", "died in a mysterious accident", "blown up by an explosions wizard", "slain by ninjas in a dark alley" ]
    death = random.choice(death_list)
    print("In the end, " + pronoun + " was " + death + ".")

# Function to Generate range dates after "in the year XXX" for use in above events
def create_date(currentStartYear, rangeEnd):
    years_range = range(currentStartYear, rangeEnd)
    return f"In the year {random.choice(years_range)}:"


#Call the functions
# Generating a Short Biography
print(title + " " + name + " was " + start + " into a " + background + " family " + "and received education at " +
      education + ". " + pronoun + " rose to power by" + rise + ".")

print(create_date(1001, 1029))
war_started()
declaration_of_war()
wealth_power()
print(monster_encounter())
death_story()
