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
    os.system("cls")


def delay_short():
    time.sleep(0.5)


def delay_medium():
    time.sleep(1)


def abandoned_mansion():

    region_builder(
        "abandoned mansion",
        """    You arrived to a place where you supposed to find farmers house.
    Instead you see that their house is ruined and abandoned.
    The property is overgrown with thick bushes, the windows are boarded up and covered with ivy,
    making it impossible to see inside. The planks on one of the windows appear broken, 
    and perhaps with a little effort you will be able to get into the house.
    If you decide to leave, you can go to The Old Farm or Plains.
    """,
        ["old farm", "plains"],
    )

    explore("Abandoned Mansion")

    abandoned_mansion()


def flat_fields():

    region_builder(
        "flat fields",
        """    You came to the flat fields. 
    To the south you see the road leading to the port, and to the west there are ruins of a castle.
    """,
        ["port", "ruins"],
    )

    explore("Flat Fields")

    flat_fields()


def iron_ore_mine():

    region_builder(
        "iron ore mine",
        """    Here is an old iron ore mine.
    A long time ago, the ore used to make the best weapons was mined here.
    Now the mine terrifies with abandoned corridors and strange sounds coming out of the depths
    """,
        ["mountains"],
    )

    explore("Iron Ore Mine")

    iron_ore_mine()


def goblin_forest():

    region_builder(
        "goblin forest",
        """    You've heard a lot about this dangerous forest.
    Many wanderers were lost here, and many merchants were robbed.
    Herds of wild goblins attack those who could not afford to hire adequate protection.
    """,
        ["swamp", "river", "plains"],
    )

    explore("Goblin Forest")

    goblin_forest()


def safe_path():

    region_builder(
        "safe path",
        """NO DESCRIPTION
    """,
        ["darkwood", "green hills"],
    )

    explore("Safe Path")

    safe_path()


def gate():

    region_builder(
        "gate",
        """NO DESCRIPTION
    """,
        ["plains"],
    )

    explore("Gate")

    gate()


def old_farm():

    region_builder(
        "old farm",
        """NO DESCRIPTION
    """,
        ["east crossroads", "south crossroads", "abandoned mansion"],
    )

    explore("Old Farm")

    old_farm()


def mill():

    region_builder(
        "mill",
        """NO DESCRIPTION
    """,
        ["river", "waterfall"],
    )

    explore("Mill")

    mill()


def waterfall():

    region_builder(
        "waterfall",
        """NO DESCRIPTION
    """,
        ["mill", "rocks"],
    )

    explore("Waterfall")

    waterfall()


def green_hills():

    region_builder(
        "green hills",
        """NO DESCRIPTION
    """,
        ["west crossroads", "clearing", "safe path", "north crossroads"],
    )

    explore("Green Hills")

    green_hills()


def clearing():

    region_builder(
        "clearing",
        """NO DESCRIPTION
    """,
        ["woods", "green hills"],
    )

    explore("Clearing")

    clearing()


def woods():

    region_builder(
        "woods",
        """NO DESCRIPTION
    """,
        ["west crossroads", "clearing", "rocks"],
    )

    explore("Woods")

    woods()


def inn():

    region_builder(
        "inn",
        """NO DESCRIPTION
    """,
        ["town"],
    )

    explore("Inn")

    inn()


def temple():

    region_builder(
        "temple",
        """NO DESCRIPTION
    """,
        ["town"],
    )

    explore("Temple")

    temple()


def medic():

    region_builder(
        "medic",
        """NO DESCRIPTION
    """,
        ["town"],
    )

    explore("Medic")

    medic()


def ruins():

    region_builder(
        "ruins",
        """NO DESCRIPTION
    """,
        ["north crossroads", "east crossroads", "flat fields"],
    )

    explore("Ruins")

    ruins()


def north_crossroads():

    region_builder(
        "north_crossroads",
        """    You have entered the northern crossroads. 
    Many merchants and adventurers travel here. 
    Most of them go north, where dangers await, but also great wealth.
    """,
        ["town", "darkwood", "green hills", "ruins"],
    )

    explore("North Crossroads")

    north_crossroads()


def south_crossroads():

    region_builder(
        "south_crossroads",
        """NO DESCRIPTION
    """,
        ["town", "plains", "river", "old farm"],
    )

    explore("South Crossroads")

    south_crossroads()


def west_crossroads():

    region_builder(
        "west_crossroads",
        """NO DESCRIPTION
    """,
        ["town", "woods", "green hills", "river"],
    )

    explore("West Crossroads")

    west_crossroads()


def east_crossroads():

    region_builder(
        "east_crossroads",
        """NO DESCRIPTION
    """,
        ["town", "ruins", "old farm", "port"],
    )

    explore("East Crossroads")

    east_crossroads()


def cave():

    region_builder(
        "cave",
        """NO DESCRIPTION
    """,
        ["mountains"],
    )

    explore("Cave")

    cave()


def dungeon():

    region_builder(
        "dungeon",
        """NO DESCRIPTION
    """,
        ["abandoned mansion"],
    )

    explore("Dungeon")

    dungeon()


def river():

    region_builder(
        "river",
        """NO DESCRIPTION
    """,
        ["west crossroads", "south crossroads", "mill", "goblin forest"],
    )

    explore("River")

    river()


def desert():

    region_builder(
        "desert",
        """NO DESCRIPTION
    """,
        ["rocks"],
    )

    explore("Desert")

    desert()


def coast():

    region_builder(
        "coast",
        """NO DESCRIPTION
    """,
        ["port"],
    )

    explore("Coast")

    coast()


def plains():

    region_builder(
        "plains",
        """NO DESCRIPTION
    """,
        ["gate", "south crossroads", "abandoned mansion", "goblin forest"],
    )

    explore("Plains")

    plains()


def swamp():

    region_builder(
        "swamp",
        """NO DESCRIPTION
    """,
        ["goblin forest"],
    )

    explore("Swamp")

    swamp()


def rocks():

    region_builder(
        "rocks",
        """NO DESCRIPTION
    """,
        ["desert", "woods", "waterfall"],
    )

    explore("Rocks")

    rocks()


def port():

    region_builder(
        "port",
        """NO DESCRIPTION
    """,
        ["east crossroads", "flat fields", "coast"],
    )

    explore("Port")

    port()


def mountains():

    region_builder(
        "mountains",
        """NO DESCRIPTION
    """,
        ["cave", "iron ore mine", "darkwood"],
    )

    explore("Mountains")

    mountains()


def darkwood():

    region_builder(
        "darkwood",
        """    You are not able to see the light of day through impenetrable thickets of forests.
    You are surrounded by darkness on all sides, you are afraid of what may be lurking in it.
    """,
        ["mountains", "safe path", "north crossroads"],
    )

    explore("The Darkwood")

    darkwood()


def town():

    region_builder(
        "town",
        """    This is small and peaceful town at a crossroads.
    The citizens are poor, but you can see that they are good people.
    You stand by the Town Gates, and see Townsquare nearby.
    You can go there and visit the local merchants, you can also leave the Town in all directions.
    """,
        ["north crossroads", "south crossroads", "west crossroads", "east crossroads"],
    )

    def explore_town():
        clear_screen()

        print(
            "You are standing in the Townsquare, you look around and you can see a shop, a medic and a temple nearby. "
        )
        print(
            "If you need additional equipment and have the right amount of money, it is worth visiting Blacksmith."
        )
        print("At the Medic you can heal your wounds and buy potions.")
        print("In the Temple you can learn new spells.")
        print("\nWhat do you do?\n")
        print("1 - Visit Shop")
        print("2 - Visit Temple.")
        print("3 - Visit Inn")
        print("\n4 - Go back to Town Gates\n")

        choice = input("> ")

        if choice == "1":
            functions.shop()

        elif choice == "2":
            functions.temple()

        elif choice == "3":
            functions.inn()

        elif choice == "4":
            town()

        else:
            print("Wrong option.")
            delay_short()
        explore_town()

    explore_town()


def region_builder(region_name, region_description, next_regions):
    clear_screen()

    where_are_you = f"\n\nYou are in The {region_name.title().replace('_', ' ')}."
    print(f"{where_are_you}")
    print(f"{'-' * len(where_are_you)}\n")
    print(f"{region_description}")

    print("\nFrom here you can travel to:\n")

    next_regions_list = []

    for number, region in enumerate(next_regions, start=1):
        print(number, "- ", region.title())
        next_regions_list.append(region)

    print(
        f"\n{len(next_regions_list)+1} -  Explore {region_name.title().replace('_', ' ')}"
    )

    print("\n--------------------")
    print("0 - Show Hero Screen")
    print("--------------------")

    try:
        input_message = int(input("\n\nWhat would you like to do?    > "))

        if input_message == len(next_regions_list) + 1:
            return

        elif input_message == 0:
            clear_screen()
            functions.player.show_player_screen()
            eval(f"{region_name}()".replace(" ", "_"))

        elif input_message < 0 or input_message > len(next_regions_list):
            print("\nWrong option!")
            delay_short()
            eval(f"{region_name}()".replace(" ", "_"))

        else:
            eval((f"{next_regions_list[input_message-1]}()".replace(" ", "_")))

    except ValueError:
        print("\nWrong option!")
        delay_short()
        eval(f"{region_name}()")


def explore(where_are_you):
    clear_screen()

    place = f"You are in {str(where_are_you)}."

    print(f"\n\n{place}")
    print(f"{'-' * len(place)}\n")
    print("What do you do?")
    print("1 - Examine the area")
    print("2 - Do nothing and go back.")
    print("0 - Hero screen.\n")

    choice = int(input("> "))

    if choice == 1:
        examine_area(where_are_you)
    elif choice == 2:
        return
    elif choice == 0:
        clear_screen()
        functions.player.show_player_screen()
    else:
        print("Wrong option.")

    explore(where_are_you)


def examine_area(where_are_you):
    clear_screen()

    print(f"You search the {where_are_you}.")
    print("The results of the search depend on your luck.")
    print("You can find valuable items or come across dangerous enemies.")
    input()

    difficulty = functions.random.randint(10, 80)

    if functions.player.luck >= difficulty:
        print("You managed to remain silent during your search.")
        print("Thanks to this, you did not alarm nearby enemies.")
        print("If there are any valuable items in this area, you should find them.")
        input()
        functions.treasure()
    else:
        print(
            "You made a lot of noise by searching the area, an enemy hiding nearby noticed you and attacked!"
        )
        input()
        functions.battle()


clear_screen()
