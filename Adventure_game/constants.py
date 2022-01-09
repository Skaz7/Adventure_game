import json
from create_characters import *

levels = [200, 450, 750, 1250]

with open(
    "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\items.json",
    "r",
) as file:
    global items
    items = json.load(file)
