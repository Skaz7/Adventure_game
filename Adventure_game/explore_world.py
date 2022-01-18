"""
Module for exploring world, which is build as separated rooms.
Player explores each room and encouters various monsters and traps.
List of regions ["woods","town","ruins","north crossroads","south crossroads","west crossroads","east crossroads","cave","dungeon",
                 "weapon shop","medic","magic shop","river","desert","mountains","seaside","plains","swamp","rocks", "green hills",
                 "mill", "old farm", "gate", "darkwood", "goblin forest", "iron ore mine", "flat fields", "abandoned mansion"]
"""


from functions import clear_screen, delay_medium


clear_screen()


def abandoned_mansion():
    print(f"You are in the Abandoned Mansion.")
    delay_medium()
    region_builder("abandoned mansion",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def flat_fields():
    print(f"You are in the Flat Fields.")
    delay_medium()
    region_builder("flat fields",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def iron_ore_mine():
    print(f"You are in the Iron Ore Mine.")
    delay_medium()
    region_builder("iron ore mine",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def goblin_forest():
    print(f"You are in the Goblin Forest.")
    delay_medium()
    region_builder("goblin forest",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def darkwood():
    print(f"You are in the Darkwood.")
    delay_medium()
    region_builder("darkwood",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def gate():
    print(f"You are at the Gate.")
    delay_medium()
    region_builder("gate",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def old_farm():
    print(f"You are in the Old Farm.")
    delay_medium()
    region_builder("old farm",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def mill():
    print(f"You are in the Mill.")
    delay_medium()
    region_builder("mill",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def green_hills():
    print(f"You are in the Green Hills.")
    delay_medium()
    region_builder("green hills",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def woods():
    print(f"You are in the Woods.")
    delay_medium()
    region_builder("woods",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def town():
    print(f"You are in the Town.")
    delay_medium()
    region_builder("town",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads", "west crossroads", "east crossroads"])

    return


def ruins():
    print(f"You are in the Ruins.")
    delay_medium()
    region_builder("ruins",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def north_crossroads():
    print(f"You are in the North Crossroads.")
    delay_medium()
    region_builder("north_crossroads",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["river", "mountains", "seaside",])

    return


def south_crossroads():
    print(f"You are in the South Crossroads.")
    delay_medium()
    region_builder("south_crossroads",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def west_crossroads():
    print(f"You are in the West Crossroads.")
    delay_medium()
    region_builder("west_crossroads",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def east_crossroads():
    print(f"You are in the East Crossroads.")
    delay_medium()
    region_builder("east_crossroads",
    """After you left town, you came to a East Crossroads.
    In the middle there is a broken signpost, from which you can barely read where the roads lead.
    It turns out that the main road continues east, to the sea.
    In the north you will find an old farm, and a path to the south will lead you to an abandoned mansion.

    What would you do?
    """,
    ["town", "flat fields", "old farm", "abandoned mansion"])
    
    return


def cave():
    print(f"You are in the Cave.")
    delay_medium()
    region_builder("cave",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def dungeon():
    print(f"You are in the Dungeon.")
    delay_medium()
    region_builder("dungeon",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def weapon_shop():
    print(f"You are in the Weapon Shop.")
    delay_medium()
    region_builder("weapon shop",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def medic():
    print(f"You are in the Medic.")
    delay_medium()
    region_builder("medic",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def magic_shop():
    print(f"You are in the Magic Shop.")
    delay_medium()
    region_builder("magic shop",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def river():
    print(f"You are in the River.")
    delay_medium()
    region_builder("river",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def desert():
    print(f"You are in the Desert.")
    delay_medium()
    region_builder("desert",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def mountains():
    print(f"You are in the Mountains.")
    delay_medium()
    region_builder("mountains",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def seaside():
    print(f"You are at the Seaside.")
    delay_medium()
    region_builder("seaside",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def plains():
    print(f"You are in the Plains.")
    delay_medium()
    region_builder("plains",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def swamp():
    print(f"You are in the Swamp.")
    delay_medium()
    region_builder("swamp",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])

    return


def rocks():
    print(f"You are in the Rocks.")
    delay_medium()
    region_builder("rocks",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def region_builder(region_name, region_description, next_regions):

    print(f"\n\nYou have reached The {region_name.capitalize()}.")
    print(f"{region_description}")
    print("\nFrom here you can go to:\n")

    next_regions_list = []

    for number, region in enumerate(next_regions, start=1):
        print(number, region.title())
        next_regions_list.append(region)

    input_message = int(input("Where are you going to?    > "))

    eval((f"{next_regions_list[input_message-1]}()".replace(" ", "_")))


region_builder("town",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads", "west crossroads", "east crossroads"])
