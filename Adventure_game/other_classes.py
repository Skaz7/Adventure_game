import functions

class Chest:
    def __init__(self, opened, trap, gold, item, exp, searched):
        self.opened = opened
        self.trap = trap
        self.gold = gold
        self.item = item
        self.exp = exp
        self.searched = searched
    
    def open(self):
        if self.opened == True:
            print("This chest was already searched. You found nothing")
            input()
        else:
            print("\nWhat would you do?")
            print("1 - Try to smash the chest")
            print("2 - Use lockpick to open it")
            print("0 - Leave it alone")

            while True:
                action = input("\n> ")
                if action == "1":
                    print("\nYou take a huge swing and hit the box with all your might.")
                    print(
                        "\nUnfortunately, the box was so delicate that it got damaged with all its contents."
                    )
                    print("\nToo bad...")
                    self.searched = True
                    input()
                    return

                elif action == "2":
                    if not any("Lockpick" in d.keys() for d in functions.player.inventory.values()):
                        print("\nYou don't have a lockpick.")
                        input()
                        return
                    else:
                        print("You opened the chest, and find some goods.")
                        del functions.player.inventory["Lockpick"]
                        self.opened = True
                        functions.player.money += self.gold
                        functions.player.inventory[self.item] = self.item.values()
                        functions.player.experience += self.exp
                        self.searched = True
                        input()
                        return

                elif action == "3":
                    return
                else:
                    print("Wrong option!")
                    input()


                

            else:
                print("\nBłędny wybór!")
                input()
                open(self)


