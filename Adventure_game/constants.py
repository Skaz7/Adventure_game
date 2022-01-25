import json
# from create_characters import *

levels = [450, 1300, 3000, 5000]

with open(
    "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\all_items.json",
    "r",
) as file:
    global all_items
    all_items = json.load(file)

player_temp_stat_boost = {"Damage": 0, "Defense": 0, "Luck": 0}

player_states = ['frozen', 'bleed', 'burn', 'poisoned', 'stunned']
