# Generates legends, random events, history for locations
# Locations can mean many things, game related, and not directly. Obvious example of location is a game room, a single map/area in a game.

import random
import location_util

# History Static Variables
area_type = ['Dungeon', 'Temple', 'Tunnel Network', 'Tavern', 'Fort', 'Town', 'Village', 'Camp']
action_list = ['Founded', 'Built', 'Extended', 'Hardship', 'Abandoned', 'Destroyed', 'Prospered'] #

def found():
   return location_util.create_date(0, 1000, False) + " " + random.choice(action_list) + " " + random.choice(area_type) + " " + location_util.print_dummy_location() + "."

print(found())


