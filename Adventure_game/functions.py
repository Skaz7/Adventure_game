import os
import random
import time


from images import *
from constants import *


def clear_screen():
    os.system("cls")


def delay_short():
    time.sleep(0.5)

def delay_medium():
    time.sleep(1.5)

def delay_long():
    time.sleep(3)


def roll_20_dice():
    # imitates 20-side dice roll
    return random.randint(1, 20)


def roll_6_dice():
    # imitates 6-side dice roll
    return random.randint(1, 6)


def start_game():
    clear_screen()

    print("To jest nowa gra.")
    print("Zacznij od stworzenia swojej postaci\n\n")

    global player
    player = create_player_character()
    decision_path()


def decision_path():

    clear_screen()

    print("\nCo chcesz zrobić?")
    print("\n1. Walka")
    print("2. Sklep")

    choice = input("> ")

    if choice == "1":
        battle()
    elif choice == "2":
        shop()
    else:
        quit()


def attack():
    """
    Chance for hit an enemy is based on hero and enemy luck, and 20-side dice roll.
    If hero hits an enemy, he gets experience points equal to hit chance and 6-side dice roll.
    When hero experience exceeds levels set in a given list, he gets a new level.
    """
    player_hit_chance = (roll_20_dice() + player.getLuck()) - (
        roll_20_dice() + enemy.getChance()
    )

    if player_hit_chance > 0:

        print(f"\nUdało Ci się zadać cios.")
        enemy_damage = roll_20_dice() + player.getAttack() - enemy.getDefense()
        player.setExperience(
            player.getExperience()
            + (player_hit_chance + roll_6_dice()) * 10 * player.getLevel() * 0.5
        )

        # Damage can't be lower than 0
        if enemy_damage < 0:
            enemy_damage == 0

        else:
            pass
        print(f"\n Przeciwnik odniósł {enemy_damage} obrażeń.")

        enemy.setHealth(int(enemy.getHealth() - enemy_damage))
        delay_short()

    else:
        print("\nNie udało Ci się zadać ciosu, przeciwnik był sprytniejszy.")
        delay_short()

    if enemy.getHealth() <= 0:
        # hero gets 10% extra experience for defeating an enemy
        player.setExperience(int(player.getExperience() * 1.1))

        for i in range(len(levels)):
            if player.getExperience() > levels[i]:
                player.level_up()

        delay_medium()
        victory()

    else:
        print(f"\nCzas na ruch przeciwnika.")
        delay_short()

        print(f"{enemy.getName()} atakuje!")
        delay_short()

        enemy_hit_chance = (roll_20_dice() + enemy.getChance()) - (
            roll_20_dice() + player.getLuck()
        )

        if enemy_hit_chance > 0:
            print("Jego cios Cię dosięgnął.")
            player_damage = roll_20_dice() + enemy.getAttack() - player.getDefense()

            if player_damage < 0:
                delay_short()
                print(f"{enemy.getName()} nie zadał Ci obrażeń...")

            else:
                delay_short()
                print(f"{enemy.getName()} zadał Ci {player_damage} obrażeń...")
                player.setHealth(player.getHealth() - player_damage)
                delay_medium()
        else:
            print(f"{enemy.getName()} nie zdołał Cię dosięgnąć.")
            delay_medium()


def magic_attack():
    """
    Chance for hit an enemy is based on hero and enemy luck, and 20-side dice roll.
    If hero hits an enemy, he gets experience points equal to hit chance and 6-side dice roll.
    When hero experience exceeds levels set in a given list, he gets a new level.
    """
    player_hit_chance = (roll_20_dice() + player.getLuck()) - (
        roll_20_dice() + enemy.getChance()
    )

    if player_hit_chance > 0:

        print(f"\nUdało Ci się zadać obrażenia magiczne.")
        enemy_damage = roll_20_dice() + player.getMagic() - enemy.getDefense()
        player.setExperience(
            player.getExperience()
            + (player_hit_chance + roll_6_dice()) * 10 * player.getLevel() * 0.5
        )

        # Damage can't be lower than 0
        if enemy_damage < 0:
            enemy_damage == 0

        else:
            pass
        print(f"\n Przeciwnik odniósł {enemy_damage} obrażeń.")
        enemy.setHealth(int(enemy.getHealth() - enemy_damage))
        delay_short()

    else:
        print("\nTwoja magia zawiodła, nie zadałeś przeciwnikowi obrażeń.")
        delay_short()

    if enemy.getHealth() <= 0:
        # hero gets 10% extra experience for defeating an enemy
        player.setExperience(int(player.getExperience() * 1.1))

        for i in range(len(levels)):
            if player.getExperience() > levels[i]:
                player.level_up()

        delay_medium()
        victory()

    else:
        print(f"\nCzas na ruch przeciwnika.")
        delay_short()

        print(f"{enemy.getName()} atakuje!")
        delay_short()

        enemy_hit_chance = (roll_20_dice() + enemy.getChance()) - (
            roll_20_dice() + player.getLuck()
        )

        if enemy_hit_chance > 0:
            print("Jego cios Cię dosięgnął.")
            player_damage = roll_20_dice() + enemy.getAttack() - player.getDefense()

            if player_damage < 0:
                delay_short()
                print(f"{enemy.getName()} nie zadał Ci obrażeń...")

            else:
                delay_short()
                print(f"{enemy.getName()} zadał Ci {player_damage} obrażeń...")
                player.setHealth(player.getHealth() - player_damage)
                delay_medium()
        else:
            print(f"{enemy.getName()} nie zdołał Cię dosięgnąć.")
            delay_medium()


def use_item():
    """
    Function for using items from Hero's inventory.
    First you have to choose item type from: weapons/armor, consumables/mixtures, magical items
    Then you choose specific item from given type
    In case of consumables, its destroyed after use and removed from inventory
    In case of weapons and armor, its durability is decreased each turn of battle, and item is destroyed afters its durability reaches 0
    """
    clear_screen()

    print("\nZ jakiego typu przedmiotu chcesz skorzystać?\n")
    print("1 - Broń / Zbroja.")
    print("2 - Mikstura, jedzenie.")
    print("3 - Inny.\n")
    print("0 - Powrót")

    choice = input("\n> ")

    def choose_item_type(item_type):
        clear_screen()

        print(f"\n\nPosiadane przez Ciebie przedmioty typu {item_type.capitalize()}:")

        # list of every item in Hero's inventory
        for k, v in player.getItems()[item_type].items():
            print(f"\n{k.capitalize()} : ")
            print("-" * (len(k) + 5))

            for x, y in v.items():
                print(f"\t{x:10} -", y)

        # create item list from dictionary keys
        item_list = list(player.getItems().get(item_type))

        print(f"\nCzego chcesz użyć w tej turze?\n")

        for i in enumerate(item_list, start=1):
            print(*i)

        try:
            choice = int(input("\n> "))

            if choice < 0 or choice > len(item_list):
                print("\nWybrałeś nieprawidłową opcję, powtórz.")
                return

            elif choice == 0:
                return

            else:
                choosed_item = item_list[choice - 1]

                if item_type == "weapons":
                    player.setAttack(
                        player.getAttack()
                        + all_items[item_type][choosed_item]["Damage"]
                    )
                    player.setDefense(
                        player.getDefense()
                        + all_items[item_type][choosed_item]["Defense"]
                    )

                    # durability of item is decreased after each use
                    player.getItems()[item_type][choosed_item]["Durability"] -= 1

                    # if item durability reaches 0, item is destroyed and removed from inventory
                    if player.getItems()[item_type][choosed_item]["Durability"] < 1:
                        del player.getItems()[item_type][choosed_item]
                    else:
                        pass

                elif item_type == "consumables":

                    # if actual health plus potion HP exceeds max health level, potion effect is reduced
                    if (
                        player.getHealth() + all_items[item_type][choosed_item]["HP"]
                        > player_max_health
                    ):
                        player.setHealth(player_max_health)

                    else:
                        player.setHealth(
                            player.getHealth()
                            + all_items[item_type][choosed_item]["HP"]
                        )

                    player.setMagic(
                        player.getMagic() + all_items[item_type][choosed_item]["MP"]
                    )

                    # consumable item is destroyed after use, and removed from inventory
                    del player.getItems()[item_type][choosed_item]

                elif item_type == 'other':

                    if 'Luck' in player.getItems()[item_type][choosed_item].keys():
                        player.setLuck(player.getLuck() + player.getItems()[item_type][choosed_item]['Luck'])

                    elif 'Clear State' in player.getItems()[item_type][choosed_item].keys():
                        player.setState([])

                    # elif '' in player.getItems()[item_type][choosed_item].keys():

                    else:
                        pass

            use_item_text = (
                f"Użyłeś przedmiotu {choosed_item}, Twoje statystyki wzrastają."
            )
            print(f"\n\n\t\t\t", "-" * (len(use_item_text) + 6))
            print(f"\t\t\t |  {use_item_text}  |")
            print(f"\t\t\t", "-" * (len(use_item_text) + 6))
            delay_medium()

        except ValueError:
            return

    if choice == "1":
        choose_item_type("weapons")

    elif choice == "2":
        choose_item_type("consumables")

    elif choice == "3":
        choose_item_type('other')

    elif choice == "0" or choice == "":
        return

    else:
        return


def defense():
    print("Obrona nie jest opcją, musisz atakować!")
    delay_medium()


def run():
    run_chance = player.getLuck() + roll_20_dice()
    stop_chance = enemy.getChance() + roll_20_dice()

    if run_chance > stop_chance:
        print(
            "\nUdało Ci się uciec z miejsca potyczki, przeciwnik nie może Cię dogonić."
        )
        delay_medium()
        decision_path()

    else:
        print(
            "\nNie udało Ci się uciec, przeciwnik był sprytniejszy i walka trwa dalej."
        )
        delay_medium()
        return


def battle():

    global enemy, player_max_health
    enemy = create_enemy()
    enemy_max_health = enemy.getHealth()
    player_max_health = player.getHealth()
    turn_counter = 0

    while True:

        clear_screen()
        turn_counter += 1

        print("\n\t\t\t\tTRWA WALKA!")
        print("\t\t\t\t===========")
        print(f"\n\t\t\t\tTura {turn_counter}")

        player_health_bar = "=" * int(player.getHealth() / 2)

        if player.getHealth() < player_max_health * 0.3:
            player_health_bar_color = "\033[0;31m"

        elif player_max_health * 0.3 <= player.getHealth() < player_max_health * 0.7:
            player_health_bar_color = "\033[0;33m"

        elif player.getHealth() >= player_max_health * 0.7:
            player_health_bar_color = "\033[0;32m"

        print(f"\nBohater - {player.getName()}")
        print("-" * (10 + len(player.getName())))
        print(f'{"Poziom:":16} {player.getLevel()}')
        print(f'{"Doświadczenie:":16} {player.getExperience()}')
        print(
            f'{"Zdrowie:":16} {player.getHealth()} {player_health_bar_color} [{player_health_bar}',
            " " * int((player_max_health - player.getHealth()) / 2),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Atak:":16} {player.getAttack()}')
        print(f'{"Obrona:":16} {player.getDefense()}')
        print(f'{"Magia:":16} {player.getMagic()}')
        print(f'{"Szczęście:":16} {player.getLuck()}')
        print(f'{"Pieniądze:":16} {player.getMoney()}')
        # print(f'{"Przedmioty:":16} {player.getItems()}\n')

        print(f"\nPrzeciwnik - {enemy.getName()}")
        print("-" * (13 + len(enemy.getName())))

        enemy_health_bar = "=" * int(enemy.getHealth() / 2)

        if enemy.getHealth() < enemy_max_health * 0.3:
            enemy_health_bar_color = "\033[0;31m"

        elif enemy_max_health * 0.3 <= enemy.getHealth() < enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;33m"

        elif enemy.getHealth() >= enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;32m"

        print(
            f'{"Zdrowie":17} {enemy.getHealth()} {enemy_health_bar_color} [{enemy_health_bar}',
            " " * int((enemy_max_health - enemy.getHealth()) / 2),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Atak":17} {enemy.getAttack()}')
        print(f'{"Obrona":17} {enemy.getDefense()}')
        print(f'{"Obrona magiczna:":17} {enemy.getMagicdefense()}')
        print(f'{"Szansa trafienia:":17} {enemy.getChance()}')

        print(f"\n--------------------------------")
        print(f"| Możliwe akcje:\t       |")
        print(f"|\t 1 - atak fizyczny     |")
        print(f"|\t 2 - atak magiczny     |")
        print(f"|\t 3 - użycie przedmiotu |")
        print(f"|\t 4 - obrona            |")
        print(f"|\t 5 - ucieczka          |")
        print(f"--------------------------------")
        print(f"\nCo robisz?")

        battle_action = input("> ")

        if battle_action == "1":
            attack()
        elif battle_action == "2":
            magic_attack()
        elif battle_action == "3":
            use_item()
        elif battle_action == "4":
            defense()
        elif battle_action == "5":
            run()
        else:
            print("Wybierz opcję z zakresu 1 - 5!")


def victory():
    clear_screen()

    print("\n\nOdniosłeś wspaniałe zwycięstwo!")
    print("\nStoisz nad zwłokami swojego przeciwnika i zastanawiasz się co dalej...")
    print("\nPostanawiasz:")
    print("\n\t1 - Przeszukać zwłoki przeciwnika.")
    print("\t2 - Zostawić go w spokoju i ruszyć dalej.")
    print("\t3 - Odwiedzić sklep.")

    choice = input("\n> ")
    if choice == "1":
        body_search()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("\nWybierz jedną z opcji 1-3 !")
        victory()


def body_search():

    money = roll_6_dice()
    player.setMoney(player.getMoney() + money)
    print(f"\nZnalazłeś {money} sztuk złota.")
    print("\nCiekawe, czy znajdzesz jeszcze jakieś przedmioty...")
    delay_medium()

    for item_type, item in all_items.items():

        for k, v in item.items():

            loot_chance = (roll_20_dice() - int(v["Price"] / 5)) - (roll_20_dice() * 2)

            if loot_chance > 0:

                print(f"Świetnie! Udało Ci się coś znaleźć!")
                delay_long()
                if k in player.getItems()[item_type]:
                    print(
                        f"\nNiestety, ale {k} posiadasz już w ekwipunku, nie możesz nieść kolejnego."
                    )
                    print("Łup zostaje na swoim miejscu.\n")
                    delay_long()

                else:
                    player.getItems()[item_type][k] = v
                    print(f"Przedmiot {k.capitalize()} został dodany do ekwipunku.")
                    delay_long()
            else:
                pass

    delay_long()
    battle()


def shop():
    def buy_item(item_type):
        clear_screen()

        items_list = []

        print("\nWybrałeś broń, oto przedmioty z tej kategorii dostępne w sprzedaży:\n")

        for number, (item, stats) in enumerate(all_items[item_type].items(), start=1):
            print(f"{number}. Przedmiot: {item}")
            print("-" * (len(f"Przedmiot: {item}") + 3))
            items_list.append(item)

            for i, j in stats.items():
                print(f"\t\t{i:11}: {j}")

        choice = int(input("\nJaki przedmiot chcesz kupić?   > ")) - 1

        item_to_buy = items_list[choice]

        for item_type, item in all_items.items():

            for k, v in item.items():

                if k == item_to_buy:

                    new_item_dict = {k: v}
                    print(new_item_dict)
                    player.getItems()[item_type].update(new_item_dict)

                else:
                    pass

        shop()

    clear_screen()

    print("\n\n\t\t\t\t\t\t", "-" * 20)
    print("\t\t\t\t\t\t|  Witaj w sklepie!  |")
    print("\t\t\t\t\t\t", "-" * 20,"\n")
    print("Posiadasz następujące przedmioty:")

    for item_type, item in player.getItems().items():

        for name, parameters in item.items():
            print(name)

    print("\n\n\nLista przedmiotów na sprzedaż:")

    for i, item_type in enumerate(all_items, start=1):
        print(f"\n{i}. {item_type.capitalize()} :")
        print(f"{'-' * (len(item_type)+6)} ")

        for k in all_items[item_type].keys():
            print("\t", k.capitalize())

    print("\n\n")

    print("\nWybierz kategorię przedmiotu, który chcesz kupić (1/2/3)")
    print("\n0 - Powrót\n")

    choice = input("\n> ")

    if choice == "1":

        buy_item("weapons")

    elif choice == "2":

        buy_item("consumables")

    elif choice == "3":

        buy_item("other")

    elif choice == "0":
        decision_path()

    else:
        print("\n\n\t\t\t\tWybrałeś nieprawidłową opcję!")
        delay_medium()
        return

    return
