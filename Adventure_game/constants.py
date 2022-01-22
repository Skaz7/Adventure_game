import json
from create_characters import *

levels = [200, 450, 900, 1300, 1900, 4000, ]

with open(
    "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\all_items.json",
    "r",
) as file:
    global all_items
    all_items = json.load(file)

player_temp_stat_boost = {"Damage": 0, "Defense": 0}