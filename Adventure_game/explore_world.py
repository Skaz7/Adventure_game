"""
Module for exploring world, which is build as separated rooms.
Player explores each room and encouters various monsters and traps.
List of regions ["woods","town","ruins","north crossroads","south crossroads","west crossroads","east crossroads","cave","dungeon",
                 "weapon shop","medic","magic shop","river","desert","mountains","seaside","plains","swamp","rocks", "green hills",
                 "mill", "old farm", "gate", "darkwood", "goblin forest", "iron ore mine", "flat fields", "abandoned mansion"]
"""


import os
import time
import functions


def clear_screen():
    os.system('cls')


def delay_short():
    time.sleep(0.5)


def abandoned_mansion():
    delay_short()
    region_builder("abandoned mansion",
    """    You arrived to a place where you supposed to find farmers house.
    Instead you see that their house is ruined and abandoned.
    You don't know if there is anything interesting in there,
    so you wonder if you should leave the area or go to check the mansion.
    """,
    ["old farm", "plains"])

    return


def flat_fields():
    delay_short()
    region_builder("flat fields",
    """    You came to the flat fields. 
    To the south you see the road leading to the port, and to the west there are ruins of a castle.
    """,
    ["port", "ruins"])

    return


def iron_ore_mine():
    delay_short()
    region_builder("iron ore mine",
    """    Here is an old iron ore mine.
    A long time ago, the ore used to make the best weapons was mined here.
    Now the mine terrifies with abandoned corridors and strange sounds coming out of the depths
    """,
    ["mountains"])

    return


def goblin_forest():
    delay_short()
    region_builder("goblin forest",
    """    You've heard a lot about this dangerous forest.
    Many wanderers were lost here, and many merchants were robbed.
    Herds of wild goblins attack those who could not afford to hire adequate protection.
    """,
    ["swamp", "river", "plains"])

    return


def safe_path():
    delay_short()
    region_builder("darkwood",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["darkwood", "green hills"])


def gate():
    delay_short()
    region_builder("gate",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["plains"])

    return


def old_farm():
    delay_short()
    region_builder("old farm",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["east crossroads", "south crossroads", "abandoned mansion"])

    return


def mill():
    delay_short()
    region_builder("mill",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["river", "waterfall"])

    return


def waterfall():
    delay_short()
    region_builder("mill",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["mill", "rocks"])

    return


def green_hills():
    delay_short()
    region_builder("green hills",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["west crossroads", "clearing", "safe path", "north crossroads"])

    return


def clearing():
    delay_short()
    region_builder("green hills",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["woods", "green hills"])

    return


def woods():
    delay_short()
    region_builder("woods",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["west crossroads", "clearing", "rocks"])

    return


def inn():
    delay_short()
    region_builder("inn",
    """    This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop, in front of you is a temple, and a medic on you right.
    """,
    ["town"])

    return


def temple():
    delay_short()
    region_builder("inn",
    """    This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop, in front of you is a temple, and a medic on you right.
    """,
    ["town"])

    return


def medic():
    delay_short()
    region_builder("inn",
    """    This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop, in front of you is a temple, and a medic on you right.
    """,
    ["town"])

    return


def ruins():
    delay_short()
    region_builder("ruins",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "east crossroads", "flat fields"])

    return


def north_crossroads():
    delay_short()
    region_builder("north_crossroads",
    """    You have entered the northern crossroads. 
    Many merchants and adventurers travel here. 
    Most of them go north, where dangers await, but also great wealth.
    """,
    ["town", "darkwood", "green hills", "ruins"])

    return


def south_crossroads():
    delay_short()
    region_builder("south_crossroads",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["town", "plains", "river", "old farm"])
    
    return


def west_crossroads():
    delay_short()
    region_builder("west_crossroads",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["town", "woods", "green hills", "river"])
    
    return


def east_crossroads():
    delay_short()
    region_builder("east_crossroads",
    """After you left town, you came to a East Crossroads.
    In the middle there is a broken signpost, from which you can barely read where the roads lead.
    It turns out that the main road continues east, to the sea.
    In the north you will find an old farm, and a path to the south will lead you to an abandoned mansion.

    What would you do?
    """,
    ["town", "ruins", "old farm", "port"])
    
    return


def cave():
    delay_short()
    region_builder("cave",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["mountains"])
    
    return


def dungeon():
    delay_short()
    region_builder("dungeon",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["abandoned mansion"])
    
    return


def weapon_shop():
    delay_short()
    region_builder("weapon shop",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["town"])
    
    return


def medic():
    delay_short()
    region_builder("medic",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["north crossroads", "south crossroads"])
    
    return


def temple():
    delay_short()
    region_builder("magic shop",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["town"])
    
    return


def river():
    delay_short()
    region_builder("river",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["west crossroads", "south crossroads", "mill", "goblin forest"])
    
    return


def desert():
    delay_short()
    region_builder("desert",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["rocks"])
    
    return


def mountains():
    delay_short()
    region_builder("mountains",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["cave", "iron ore mine", "darkwood"])
    
    return


def coast():
    delay_short()
    region_builder("seaside",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["port"])
    
    return


def plains():
    delay_short()
    region_builder("plains",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["gate", "south crossroads", "abandoned mansion", "goblin forest"])
    
    return


def swamp():
    delay_short()
    region_builder("swamp",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["goblin forest"])

    return


def rocks():
    delay_short()
    region_builder("rocks",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["desert", "woods", "waterfall"])
    
    return


def port():
    delay_short()
    region_builder("port",
    """This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is weapon shop
    """,
    ["east crossroads", "flat fields", "coast"])


def darkwood():
    delay_short()
    region_builder("darkwood",
    """    You are not able to see the light of day through impenetrable thickets of forests.
    You are surrounded by darkness on all sides, you are afraid of what may be lurking in it.
    """,
    ["mountains", "safe path", "north crossroads"])

    clear_screen()
    print(f"It's so dark all around that you can't see much.")
    print(f"You are wondering if you can search the pile of broken wood standing on the side.")
    print("What do you do?")
    print("1 - Search the woods")
    print("2 - Leave it alone and go further.")
    choice = int(input('> '))
    if choice == 1:
        functions.battle()
    if choice == 2:
        input("pizdeczka")
    else:
        print('Wrong option.')


def town():
    delay_short()
    region_builder("town",
    """    This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand in the middle of townsquare.
    On your left there is inn, in front of you is a temple, and a medic on you right.
    You can leave the Town in all directions.
    """,
    ["north crossroads", "south crossroads", "west crossroads", "east crossroads", "inn", "temple", "shop"])


def region_builder(region_name, region_description, next_regions):
    clear_screen()

    where_are_you = f"\n\nYou are in The {region_name.title().replace('_', ' ')}."
    print(f"{where_are_you}")
    print(f"{'-' * len(where_are_you)}\n")
    print(f"{region_description}")
    delay_short()

    print("\nFrom here you can go to:\n")

    next_regions_list = []

    for number, region in enumerate(next_regions, start=1):
        print(number, '- ', region.title())
        next_regions_list.append(region)

    print(f"\n{len(next_regions_list)+1} -  Explore {region_name.title().replace('_', ' ')}")
    input_message = int(input("\nWhere yould you like to go?    > "))

    if input_message == len(next_regions_list)+1:
        print('Udało się!')

    else:
        eval((f"{next_regions_list[input_message-1]}()".replace(" ", "_")))

clear_screen()
