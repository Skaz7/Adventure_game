import os
import time
from functions import player

def clear_screen():
    os.system('cls')


def examine_dungeon():
    clear_screen()

    print("""\nYou entered the dungeon area.
You barely see anything in the dark, perhaps using a torch will help you find your way around.
The only thing you can indentify is a pile of wooden door scraps.
Maybe it better to go back and prepare yourself to examine the dungeon...
What would you do?
    """)
    print("1 - Use a torch to light your way.")
    print("2 - Use fire spell on wooden pile.")
    print("3 - Take one wooden pole and use it as a torch.")
    print("\n0 - Go back.\n")

    choice = input("> ")

    if choice == "1":
        if "Torch" in player.items:
            print("\nYou light a torch. Now you can see much better.")
            explore_dungeon()
    elif choice == "2":
        pass
    elif choice == "3":
        print("\nWhich spell will you use?")
        spellbook_list = [spell for spell in player.spellbook.keys()]
        print(spellbook_list)
    elif choice == "0":
        return
    else:
        print("\n\nWrong option!\n\n")
        time.sleep(1)
        examine_dungeon()

def explore_dungeon():
    pass
    
examine_dungeon()