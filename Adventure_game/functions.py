import os
import random
import time

from images import *
from constants import *
from create_characters import *
from explore_world import *


def clear_screen():
    os.system("cls")


def delay_short():
    time.sleep(0.5)


def delay_medium():
    time.sleep(1.5)


def delay_long():
    time.sleep(3)


def roll_20_dice():
    return random.randint(1, 20)


def roll_6_dice():
    return random.randint(1, 6)


def start_game():
    clear_screen()

    game_title = "first rpg adventure"

    print(f'\n\n\n{"=" * (len(game_title) + 4):^120}')
    print(f'{"|" + " " * (len(game_title) + 4) + "|":^120}')
    print(f'{"|  " + game_title.upper() + "  |":^120}')
    print(f'{"|" + " " * (len(game_title) + 4) + "|":^120}')
    print(f'{"=" * (len(game_title) + 4):^120}\n\n\n')

    print(f'{"Wybierz opcję:          ":^120}\n')
    print(f'{"1 - Nowa gra            ":^120}')
    print(f'{"2 - Wczytaj zapisaną grę":^120}\n')
    print(f'{"Twój wybór:             ":^120}\n')
    choice = input(f'\t\t\t\t\t\t> ')

    if choice == '1':
        global player
        player = create_player_character()
        town()
    elif choice == '2':
        print(f'\n{"FUNKCJA JESZCZE NIE DZIAŁA":^120}')
        delay_medium()
        start_game()
    else:
        print(f'\n{"WYBRAŁEŚ NIEPRAWIDŁOWĄ OPCJĘ!":^120}')
        delay_medium()
        start_game()

def hero_attack():
    """
    Chance for hit an enemy is based on hero and enemy luck, and 20-side dice roll.
    If hero hits an enemy, he gets experience points equal to hit chance and 6-side dice roll.
    When hero experience exceeds levels set in a given list, he gets a new level.
    """
    player_hit_chance = (roll_20_dice() + player.luck) - (roll_20_dice() + enemy.chance)

    if player_hit_chance > 0:

        print(f"\nTwój atak się powiódł.")
        enemy_damage = roll_20_dice() + player.attack - enemy.defense
        player.experience = player.experience + int(
            (player_hit_chance + roll_6_dice()) * 5 * player.level * 0.5
        )

        if enemy_damage < 0:
            enemy_damage == 0

        else:
            critical_chance = random.randint(0, 100)

            if critical_chance > 90:
                print(
                    f"\nUdało Ci się zadać krytyczny cios. Przeciwnik odniósł {int(enemy_damage * 2)} obrażeń."
                )
                enemy.health = int(enemy.health - int(enemy_damage * 2))
                delay_short()

            else:
                print(f"\nPrzeciwnik odniósł {enemy_damage} obrażeń.")
                enemy.health = int(enemy.health - enemy_damage)
                delay_short()

    else:
        print("\nNie udało Ci się zadać ciosu, przeciwnik był sprytniejszy.")
        delay_short()

    # player stats increased by used item are going back to previous level
    player.attack = player.attack - player_temp_stat_boost["Damage"]
    player.defense = player.defense - player_temp_stat_boost["Defense"]
    player.luck = player.luck - player_temp_stat_boost["Luck"]

    # stats boost is reset
    player_temp_stat_boost["Damage"] = 0
    player_temp_stat_boost["Defense"] = 0
    player_temp_stat_boost["Luck"] = 0

    if enemy.health <= 0:
        # hero gets 10% extra experience for defeating an enemy
        player.experience = int(player.experience * 1.1)

        if player.experience > levels[0]:
            clear_screen()
            player.level_up()
            del levels[0]

        delay_short()
        victory()

    else:
        enemy_attack()


def hero_magic_attack():
    """
    Chance for hit an enemy is based on hero and enemy luck, and 20-side dice roll.
    If hero hits an enemy, he gets experience points equal to hit chance and 6-side dice roll.
    When hero experience exceeds levels set in a given list, he gets a new level.
    """
    player_hit_chance = (roll_20_dice() + player.luck) - (roll_20_dice() + enemy.chance)

    if player_hit_chance > 0:

        print(f"\nUdało Ci się zadać obrażenia magiczne.")
        enemy_damage = roll_20_dice() + player.magic - enemy.defense
        player.experience = (
            player.experience
            + (player_hit_chance + roll_6_dice()) * 5 * player.level
        )

        # Damage can't be lower than 0
        if enemy_damage < 0:
            enemy_damage == 0

        else:
            pass
        print(f"\nPrzeciwnik odniósł {enemy_damage} obrażeń.")
        enemy.health = int(enemy.health - enemy_damage)
        delay_short()

    else:
        print("\nTwoja magia zawiodła, nie zadałeś przeciwnikowi obrażeń.")
        delay_short()

    if enemy.health <= 0:
        # hero gets 10% extra experience for defeating an enemy
        player.experience = int(player.experience * 1.1)

        if player.experience > levels[0]:
            clear_screen()
            player.level_up()
            del levels[0]

        delay_short()
        victory()

    else:
        enemy_attack()


def enemy_attack():
    print(f"\nCzas na ruch przeciwnika.")
    delay_short()

    print(f"{enemy.name} atakuje!")
    delay_short()

    enemy_hit_chance = (roll_20_dice() + enemy.chance) - (roll_20_dice() + player.luck)

    if enemy_hit_chance > 0:
        print("Jego cios Cię dosięgnął.")
        player_damage = roll_20_dice() + enemy.attack - player.defense

        if player_damage < 0:
            delay_short()
            print(f"{enemy.name} nie zadał Ci obrażeń...")
            delay_short()

        else:
            critical_chance = roll_6_dice()

            if critical_chance > 2:
                print(f"{enemy.name} zadał Ci {int(player_damage * 1.2)} obrażeń.")
                print(
                    f"\nNiestety zadał krytyczny cios, powodując u Ciebie {enemy.special}."
                )
                player.health = player.health - int(player_damage * 1.2)
                delay_medium()

                set_player_state()

                if player.health <= 0:
                    defeat()
                delay_short()
            else:
                print(f"{enemy.name} zadał Ci {player_damage} obrażeń...")
                player.health = player.health - player_damage
                if player.health <= 0:
                    defeat()
                delay_short()
    else:
        print(f"{enemy.name} nie zdołał Cię dosięgnąć.")
        delay_short()

    check_player_state()


def check_player_state():

    if len(player.state) == 0:
        pass
    else:
        condition = f"player.{player.state[0].lower()}()"
        eval(condition)


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
        for k, v in player.inventory[item_type].items():
            print(f"\n{k.capitalize()} : ")
            print("-" * (len(k) + 5))

            for x, y in v.items():
                print(f"\t{x:10} -", y)

        # create item list from dictionary keys
        item_list = list(player.inventory.get(item_type))
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
                choosed_item_data = player.inventory[item_type][item_list[choice - 1]]
                choosed_item_name = item_list[choice - 1]

                if "Damage" in choosed_item_data:
                    player.attack = player.attack + choosed_item_data["Damage"]

                    player_temp_stat_boost["Damage"] = choosed_item_data["Damage"]

                elif "Defense" in choosed_item_data:
                    player.defense = player.defense + choosed_item_data["Defense"]

                    player_temp_stat_boost["Defense"] = choosed_item_data["Defense"]

                elif "HP" in choosed_item_data:
                    # if actual health plus potion HP exceeds max health level, potion effect is reduced
                    if player.health + choosed_item_data["HP"] > player.maxhealth:
                        player.health = player.maxhealth

                    else:
                        player.health = player.health + choosed_item_data["HP"]

                elif "MP" in choosed_item_data:
                    player.magic = player.magic + choosed_item_data["MP"]

                elif "Luck" in choosed_item_data.keys():
                    player.luck = player.luck + choosed_item_data["Luck"]
                    player_temp_stat_boost["Luck"] = choosed_item_data["Luck"]

                elif "Clear State" in choosed_item_data.keys():
                    player.state = []

                elif "Cure Poison" in choosed_item_data.keys():
                    player.state.remove("poisoned")

                elif "Cure Burn" in choosed_item_data.keys():
                    player.state.remove("burned")

                elif "Bandage" in choosed_item_data.keys():
                    player.state.remove("bleed")

                elif "Teleport" in choosed_item_data.keys():
                    destination = list(choosed_item_data.values())[0]
                    # delete teleport scroll after use
                    del choosed_item_data
                    teleport(destination)

                else:
                    pass

            use_item_text = (
                f"Użyłeś przedmiotu {choosed_item_name}, Twoje statystyki wzrastają."
            )
            print(f"\n\n\t\t\t", "-" * (len(use_item_text) + 6))
            print(f"\t\t\t |  {use_item_text}  |")
            print(f"\t\t\t", "-" * (len(use_item_text) + 6))

            delay_short()

            # durability of item is decreased after each use. Consumables are destroyed after one use
            choosed_item_data["Durability"] -= 1

            # if item durability reaches 0, item is destroyed and removed from inventory
            if choosed_item_data["Durability"] < 1:
                print(f"\n\t\t\t\t  Przedmiot {choosed_item_name} został zniszczony!\n")
                del player.inventory[item_type][f"{choosed_item_name}"]
            delay_medium()

        except ValueError:
            return

    if choice == "1":
        choose_item_type("weapons")

    elif choice == "2":
        choose_item_type("consumables")

    elif choice == "3":
        choose_item_type("other")

    elif choice == "0" or choice == "":
        return

    else:
        return


def defense():
    pass


def set_player_state():
    if len(player.state) == 0:
        player.state.append(enemy.special)

    else:
        pass


def battle():

    global enemy
    enemy = create_enemy()

    while enemy.level > player.level + 1 or enemy.level < player.level - 1:
        enemy = create_enemy()

    enemy_max_health = enemy.health
    # player.maxhealth = player.health
    turn_counter = 0

    while player.health > 0 and enemy.health > 0:

        clear_screen()
        turn_counter += 1

        print("\n\t\t\t\tTRWA WALKA!")
        print("\t\t\t\t===========")
        print(f"\n\t\t\t\tTura {turn_counter}")

        player_health_bar = "=" * int(player.health * 60 / player.maxhealth)

        if player.health < player.maxhealth * 0.3:
            player_health_bar_color = "\033[0;31m"

        elif player.maxhealth * 0.3 <= player.health < player.maxhealth * 0.7:
            player_health_bar_color = "\033[0;33m"

        elif player.health >= player.maxhealth * 0.7:
            player_health_bar_color = "\033[0;32m"

        print(f"\nBohater - {player.name}")
        print("-" * (10 + len(player.name)))
        print(f'{"Poziom":19} : {player.level}')
        print(f'{"Doświadczenie":19} : {player.experience:<4} /  {levels[0]:<4}')
        print(
            f'{"Zdrowie":19} : {player.health:<4} /  {player.maxhealth:<4} {player_health_bar_color} [{player_health_bar}',
            " " * (60 - len(player_health_bar)),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Atak":19} : {player.attack}')
        print(f'{"Obrona":19} : {player.defense}')
        print(f'{"Magia":19} : {player.magic}')
        print(f'{"Szczęście":19} : {player.luck}')
        print(f'{"Pieniądze":19} : {player.money}')
        if len(player.state) == 0:
            print(f'{"Twój stan":19} : Wszystko w porządku, brak dodatkowych obrażeń.')
        else:
            print(
                f'{"Twój stan":19} : {player.state[0].capitalize()}  -   otrzymujesz dodatkowe obrażenia po każdej turze.'
            )
        print(f"\nPrzeciwnik - {enemy.name}")
        print("-" * (13 + len(enemy.name)))

        enemy_health_bar = "=" * int(enemy.health * 60 / enemy_max_health)

        if enemy.health < enemy_max_health * 0.3:
            enemy_health_bar_color = "\033[0;31m"

        elif enemy_max_health * 0.3 <= enemy.health < enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;33m"

        elif enemy.health >= enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;32m"

        print(f'{"Poziom":19} : {enemy.level}')
        print(
            f'{"Zdrowie":19} : {enemy.health:<4} /  {enemy_max_health:<4} {enemy_health_bar_color} [{enemy_health_bar}',
            " " * (60 - len(enemy_health_bar)),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Atak":19} : {enemy.attack}')
        print(f'{"Obrona":19} : {enemy.defense}')
        print(f'{"Obrona magiczna:":19} : {enemy.magicdefense}')
        print(f'{"Szansa trafienia:":19} : {enemy.chance}')
        print(f'{"Zdolność specjalna":19} : {enemy.special.capitalize()}')

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
            hero_attack()

        elif battle_action == "2":
            hero_magic_attack()

        elif battle_action == "3":
            use_item()

        elif battle_action == "4":
            defense()

        elif battle_action == "5":
            run_chance = player.luck + roll_20_dice()
            stop_chance = enemy.chance + roll_20_dice()

            if run_chance > stop_chance:
                print(
                    "\nUdało Ci się uciec z miejsca potyczki, przeciwnik nie może Cię dogonić."
                )
                delay_medium()
                if player.experience > levels[0]:
                    clear_screen()
                    player.level_up()
                    del levels[0]
                return

            else:
                print(
                    "\nNie udało Ci się uciec, przeciwnik był sprytniejszy i walka trwa dalej."
                )
                delay_medium()
                pass
        else:
            print("Wybierz opcję z zakresu 1 - 5!")

    return


def teleport(destination):
    eval(f"{destination.lower()}()")


def victory():
    clear_screen()

    print("\n\nOdniosłeś wspaniałe zwycięstwo!")
    print("\nStoisz nad zwłokami swojego przeciwnika i zastanawiasz się co dalej...")
    print("\nPostanawiasz:")
    print(
        "\n\t1 - Przeszukać zwłoki przeciwnika, chociaż nie wiesz czego się spodziewać."
    )
    print("\t2 - Zostawić go w spokoju i ruszyć dalej.")

    choice = input("\n> ")

    if choice == "1":
        body_search()

    elif choice == "2":
        return

    else:
        print("\nWybierz jedną z opcji 1-2 !")
        delay_medium()
        victory()


def defeat():
    clear_screen()
    delay_short()
    print(f"\n\n{player.name}, poniosłeś porażkę w walce i umierasz...")
    delay_short()
    print("Twoje zwłoki zostają na pożarce sępom.\n\n\n\n")
    delay_short()
    quit()


def body_search():

    risk = roll_20_dice()

    # when risk dice roll fails, player looses some HP
    if risk < 3:
        print("Uruchomiłeś pułapkę!")
        delay_short()
        print("Odniosłeś poważne obrażenia.")
        delay_short()
        print(f"\nTwoje zdrowie trwale obniża się o {20 - risk} punktów życia.")
        player.health = player.health - (20 - risk)
        if player.health < 1:
            defeat()
        delay_medium()
        return
    else:
        # player gets loot from enemy body
        money = roll_6_dice() * 2
        player.money = player.money + money
        print(f"\nZnalazłeś {money} sztuk złota.")
        print("\nCiekawe, czy znajdzesz jeszcze jakieś przedmioty...")
        delay_short()

        for item_type, item in all_items.items():

            for k, v in item.items():

                loot_chance = (roll_20_dice() - int(v["Price"] / 5)) - (
                    roll_20_dice() * 2
                )

                if loot_chance > 0:

                    print(f"Świetnie! Udało Ci się coś znaleźć!")
                    delay_short()
                    if k in player.inventory[item_type]:
                        print(
                            f"\nNiestety, ale {k} posiadasz już w ekwipunku, nie możesz nieść kolejnego.\n"
                        )
                        print("Łup zostaje na swoim miejscu.\n")
                        delay_medium()

                    else:
                        player.inventory[item_type][k] = v
                        print(f"Przedmiot {k.capitalize()} został dodany do ekwipunku.\n")
                        delay_medium()
                else:
                    pass

        delay_medium()
        return


def shop():
    
    def buy_item(item_type):
        clear_screen()

        items_list = []

        print(f"\nTwoja gotówka to {player.money}szt złota")
        print(
            f"\nWybrałeś {item_type}, oto przedmioty z tej kategorii dostępne w sprzedaży:\n"
        )

        for number, (item, stats) in enumerate(all_items[item_type].items(), start=1):
            print(f"\n{number}. Przedmiot: {item}")
            print("-" * (len(f"Przedmiot: {item}") + 3))
            items_list.append(item)

            for i, j in stats.items():
                print(f"\t\t\t{i:11}: {j}")

        try:
            choice = int(input("\nJaki przedmiot chcesz kupić?   > ")) - 1

            if choice == "":
                return

            elif choice < 0 or choice > len(items_list) - 1:
                print("\nWybrałeś nieprawidłową opcję, powtórz.")
                delay_medium()

            else:
                item_to_buy = items_list[choice]
                cost_of_item_to_buy = all_items[item_type][item_to_buy]["Price"]

                if item_to_buy in player.inventory[item_type]:
                    print('Posiadasz już ten przedmiot, nie możesz go kupić.')
                    delay_medium()
                    
                else:
                    if cost_of_item_to_buy > player.money:

                        print(
                            f"\nMasz za mało pieniedzy, brakuje Ci {cost_of_item_to_buy - player.money} sztuk złota!"
                        )
                        delay_medium()

                    else:

                        for item_type, item in all_items.items():
                            for k, v in item.items():
                                if k == item_to_buy:
                                    new_item_dict = {k: v}

                                    bought_message = f"\nKupiłeś przedmiot {item_to_buy}. Pozostało Ci {player.money - cost_of_item_to_buy} sztuk złota."

                                    print("-" * len(bought_message))
                                    print(bought_message)
                                    print("_" * len(bought_message))
                                    player.inventory[item_type].update(new_item_dict)
                                    player.money = player.money - cost_of_item_to_buy
                                    delay_medium()

                                else:
                                    pass
        except ValueError:
            print("\nWybrałeś nieprawidłową opcję, powtórz.")
            delay_medium()

        shop()

    def sell_item():
        clear_screen()

        inventory_list = []

        print("Posiadasz następujące przedmioty:")

        for item_type, item in player.inventory.items():
            for name, parameters in item.items():
                inventory_list.append(name)

        for i, item in enumerate(inventory_list, start=1):
            print(i, item)

        print(f"\nTwoja gotówka to {player.money} sztuk złota.\n\n")

        choice = int(input("\nKtóry przedmiot chcesz sprzedać?   > ")) - 1

        if choice == "":
            return

        elif choice < 0 or choice > len(inventory_list) - 1:
            print("\nWybrałeś nieprawidłową opcję, powtórz.")
            delay_medium()

        else:
            item_to_sell = inventory_list[choice]

            if item_to_sell in player.inventory["weapons"]:
                player.money = player.money + int(
                    player.inventory["weapons"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["weapons"][item_to_sell]

            elif item_to_sell in player.inventory["consumables"]:
                player.money = player.money + int(
                    player.inventory["consumables"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["consumables"][item_to_sell]

            elif item_to_sell in player.inventory["other"]:
                player.money = player.money + int(
                    player.inventory["other"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["other"][item_to_sell]

            else:
                pass
            
            print(f"\nUdało się sprzedać przedmiot {item_to_sell}.")
            inventory_list.remove(item_to_sell)
            delay_medium()

    def buy():
        clear_screen()
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

        elif choice == "0" or choice == "":
            pass

        else:
            print("\n\n\t\t\t\tWybrałeś nieprawidłową opcję!")
            delay_medium()
            return

    clear_screen()

    print("\n\n\t\t\t\t\t\t", "-" * 20)
    print("\t\t\t\t\t\t|  Witaj w sklepie!  |")
    print("\t\t\t\t\t\t", "-" * 20, "\n")
    print("Posiadasz następujące przedmioty:")

    for item_type, item in player.inventory.items():

        for name, parameters in item.items():
            print(name)

    print(f"\nTwoja gotówka to {player.money} sztuk złota.")
    print("\nCo chcesz zrobić?")
    print("\n1 - Kupić przedmiot")
    print("2 - Sprzedać przedmiot")
    print("\n0 - Powrót")

    choice = input("> ")

    if choice == "1":
        buy()
    elif choice == "2":
        sell_item()
    elif choice == "0":
        return
    else:
        print("\nWybrałeś nieprawidłową opcję!")
        delay_medium()
        shop()


def temple():
    clear_screen()

    heal_cost = 20

    print(f'\n\n{"Welcome to the Temple.":^120}')
    print(f'{"-"*24:^120}\n\n')
    print("\tHere you can heal you wounds and buy spells.")
    print("\tWhat would you like to do?\n")
    print(f"\n\t1 - Heal (costs {heal_cost} coins)")
    print("\t2 - Buy spells")
    print("\n\t0 - Leave Temple.")

    choice = input("\n\t> ")

    if choice == "0":
        return

    elif choice == "1":
        player.health = player.maxhealth
        player.state = []
        if player.money < 20:
            print(f"You don't have enough money!")
            delay_medium()
            pass
        else:
            player.money -= 20
            player.health = player.maxhealth
            player.state = []
            print("\t\t\nYou ragained all your health and healed your wounds.")
            delay_medium()
        temple()

    elif choice == "2":
        print("\nThere are no spells for sale at this time. Please come back later.")
        delay_medium()
        temple()
    else:
        print("\n\t\tWrong option!")
        delay_medium()
        temple()


def inn():
    pass
