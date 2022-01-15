import json
from create_characters import *

levels = [200, 450, 750, 1250]

with open(
    "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\all_items.json",
    "r",
) as file:
    global all_items
    all_items = json.load(file)
