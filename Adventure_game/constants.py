import json


with open(
    "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\all_items.json",
    "r",
) as file:
    # global all_items
    all_items = json.load(file)

player_temp_stat_boost = {"Damage": 0, "Defense": 0, "Luck": 0, "Magic": 0}

player_states = ["frozen", "bleed", "burn", "poisoned", "stunned"]

all_offensive_spells = {"Sparks": {"element":"fire", "power": 10, "weakness": "freeze", "mana cost": 5, "level": 1},
                        "Fireball": {"element":"fire", "power": 20, "weakness": "freeze", "mana cost": 10, "level": 3},
                        "Fire Wind": {"element":"fire", "power": 40, "weakness": "freeze", "mana cost": 20, "level": 5},
                        "Meteor Shower": {"element":"fire", "power": 70, "weakness": "freeze", "mana cost": 30, "level": 7},
                        "Magic blade": {"element":"bleed", "power": 10, "weakness": "stunned", "mana cost": 5, "level": 1},
                        "Bloody Thorns": {"element":"bleed", "power": 20, "weakness": "stunned", "mana cost": 10, "level": 3},
                        "Knock Down": {"element":"bleed", "power": 40, "weakness": "stunned", "mana cost": 20, "level": 5},
                        "Crushing Blow": {"element":"bleed", "power": 70, "weakness": "stunned", "mana cost": 30, "level": 7},
                        "Cold": {"element":"freeze", "power": 10, "weakness": "burn", "mana cost": 5, "level": 1},
                        "Frosty Cut": {"element":"freeze", "power": 20, "weakness": "burn", "mana cost": 10, "level": 3},
                        "Ice Power": {"element":"freeze", "power": 30, "weakness": "burn", "mana cost": 15, "level": 5},
                        "Winter Blizzard": {"element":"freeze", "power": 50, "weakness": "burn", "mana cost": 23, "level": 6},
                        "Avalanche": {"element":"freeze", "power": 70, "weakness": "burn", "mana cost": 30, "level": 7},
                        "Sting": {"element":"poison", "power": 10, "weakness": "none", "mana cost": 5, "level": 1},
                        "Poisonous Touch": {"element":"poison", "power": 20, "weakness": "none", "mana cost": 10, "level": 3},
                        "Rotten Blade": {"element":"poison", "power": 40, "weakness": "none", "mana cost": 20, "level": 5},
                        "Green Rain": {"element":"poison", "power": 70, "weakness": "none", "mana cost": 30, "level": 7}
                        }

all_defensive_spells = {"Minor Regeneration": {"HP": 20, "mana cost": 5, "level": 1},
                        "Greater Regeneration": {"HP": 80, "mana cost": 15, "level": 3},
                        "Cure Desease": {"Cure state": 1, "mana cost": 15, "level": 5}
                        }


levels = [450, 1300, 3000, 5000]

escape_from_battle = False