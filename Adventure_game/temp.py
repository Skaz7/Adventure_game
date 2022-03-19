import os
from re import search
import time
from create_characters import create_player_character
from other_classes import *

player = create_player_character()

def clear_screen():
    os.system("cls")


def dungeon_entrance():
    clear_screen()
    
    def burn_pile():
        print("You used a fire spell of wooden pile.")
        print(
            "The fire was enormous, and after it expired, you saw a metal box in the remaining ashes"
        )
        print("\nWhat would you do?")
        print("1 - Examine the box")
        print("2 - Leave it alone")



    while True:
        if not dungeon_entrance in functions.searched_rooms:
            print(
                """\nYou entered the dungeon area.
        You barely see anything in the dark, perhaps using a torch will help you find your way around.
        The only thing you can indentify is a pile of wooden door scraps.
        Maybe it better to go back and prepare yourself to examine the dungeon...
        What would you do?
            """
            )
            print("1 - Use a torch to light your way.")
            print("2 - Use fire spell on wooden pile.")
            print("3 - Take one wooden pole and use it as a torch.")
            print("\n0 - Go back.\n")

            choice = input("> ")

            if choice == "1":
                if "Torch" in functions.player.inventory.items():
                    print("\nYou light a torch. Now you can see much better.")
                    input()
                    explore_dungeon()
                else:
                    print("\nYou don't have a torch. You must try something else.")
                    input()
                    explore_dungeon()
            elif choice == "2":
                burn_pile()
            elif choice == "3":
                for spell, parameters in functions.player.spellbook.items():
                    if "fire" in parameters.values():
                        print("\nYou have spell that can start a fire")
                        input()
                    else:
                        print("You dont't have spell that can start a fire")
                        input()
            elif choice == "0":
                return
            else:
                print("\n\nWrong option!\n\n")
                time.sleep(1)
                dungeon_entrance()

        elif dungeon_entrance in functions.searched_rooms:
            print(
                """\nYou're standing the dungeon entrance.
        You barely see anything in the dark, perhaps using a torch will help you find your way around.
        You can see the remains of a wooden pile and a metal box that you destroyed.
        What would you do?
            """
            )
            print("1 - Use a torch to light your way.")
            print("2 - Take one wooden pole and use it as a torch.")
            print("\n0 - Go back.\n")

            choice = input("> ")

            if choice == "1":
                if "Torch" in functions.player.inventory:
                    print("\nYou light a torch. Now you can see much better.")
                    explore_dungeon()
                else:
                    print("\nYou don't have a torch.")

            elif choice == "2":
                spellbook_list = [spell for spell in functions.player.spellbook.keys()]
                for i, spell in enumerate(spellbook_list):
                    print(f"{i}. {spell}")
                print("\nWhich spell will you use?")
                choice = int(input("\n> ")) - 1
                print(f"You choosed {spellbook_list[choice]}")
                input()

            elif choice == "0":
                return
            else:
                print("\n\nWrong option!\n\n")
                time.sleep(1)
                dungeon_entrance()


def explore_dungeon():
    pass


def poison_spikes_trap():
    clear_screen()
    print("You were not perceptive enough and you set up a trap!")
    print("Poisoned needle strikes from barely visible hole in the wall.")
    print("The needle hits you in no time, you immediately feel nauseous and dizzy")
    health_lost = player.maxhealth * 0.2
    if health_lost >= player.health:
        print(f"You lost {health_lost} HP and you DIED...")
        print("\n\n\t\t\t\t========= GAME OVER =========")
        quit()
    else:
        print(f"You lost {health_lost} HP")
        print("You should use healing spell or item to recover, otherwise you can die.")
        time.sleep(1)
        if not "Cure Poison" in player.items["consumables"].values():
            print("\nYou don't have any items that could heal you.")
            input()
        else:
            print("You have some items that can heal you.")
            input()


def covered_pit_trap():
    pass


def exploding_trap():
    pass


dungeon_entrance()
