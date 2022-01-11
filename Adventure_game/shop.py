from constants import items
import time


def shop():
    clear_screen()

    print("\n\n\t\t\t\t\t\t", "-" * 20)
    print("\t\t\t\t\t\t|  Witaj w sklepie!  |")
    print("\t\t\t\t\t\t", "-" * 20)
    print()

    print("\n\n\nLista przedmiotów na sprzedaż:")

    for i, item_type in enumerate(items, start=1):
        print(f"\n{i}. {item_type.capitalize()} :")
        print(f"{'-' * (len(item_type)+6)} ")
        for k in items[item_type].keys():
            print("\t", k.capitalize())
    print("\n\n")

    print("\nWybierz kategorię przedmiotu, który chcesz kupić (1/2/3):")
    choice = input("\n> ")

    if choice == "1":

        item_type = "weapons"
        print("\nWybrałeś broń, oto przedmioty z tej kategorii dostępne w sprzedaży:\n")

        for number, (item, stats) in enumerate(items[item_type].items(), start = 1):
            print(f'{number}. Przedmiot: {item}')
            print('-' * (len(f'Przedmiot: {item}') + 3))

            for i,j  in stats.items():
                print(f'\t\t{i:11}: {j}')
            print()
        input()
        shop()

    elif choice == "2":

        item_type = "consumables"
        items_list = []
        print("\nWybrałeś mikstury, oto przedmioty z tej kategorii dostępne w sprzedaży:\n")

        for number, (item, stats) in enumerate(items[item_type].items(), start = 1):
            print(f'{number}. Przedmiot: {item}')
            print('-' * (len(f'Przedmiot: {item}') + 3))
            items_list.append(item)

            for i,j  in stats.items():
                print(f'\t\t\t{i:6}: {j}')

        print(items_list)
        choice = int(input('\nJaki przedmiot chcesz kupić?   > ')) - 1
        item_to_buy = items_list[choice]
        print(item_to_buy)
        player.items().update(items[item_type][item_to_buy])
        input()

    elif choice == "3":
        item_type = "other"
        print("\nWybrałeś inne, oto przedmioty z tej kategorii dostępne w sprzedaży:\n")

        for number, (item, stats) in enumerate(items[item_type].items(), start = 1):
            print(f'{number}. Przedmiot: {item}')
            print('-' * (len(f'Przedmiot {item}') + 3))

            for i, j in stats.items():
                print(f'\t\t\t{i:10}: {j}')

        input()
        shop()

    else:
        print("\n\n\t\t\t\tWybrałeś nieprawidłową opcję!")
        time.sleep(1)
        return

    return
