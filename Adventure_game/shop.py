from functions import clear_screen, roll_20_dice, roll_6_dice
from constants import items

clear_screen()


def shop():

    print("\n\n\t\t\t\t", "-" * 20)
    print("\t\t\t\t|  Witaj w sklepie!  |")
    print("\t\t\t\t", "-" * 20)
    print()

    print("\nLista przedmiotów na sprzedaż:")

    for item_type, item in items.items():
        print(item_type.capitalize(), ':')
        for k in item.keys():
            print(k)


shop()