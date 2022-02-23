import functions

class Chest:
    def __init__(self, opened, trap, puzzle, gold, item, exp, searched):
        self.opened = opened
        self.trap = trap
        self.puzzle = puzzle
        self.gold = gold
        self.item = item
        self.exp = exp
        self.searched = searched
    
    def open(self):
        if self.opened == True:
            pass
        else:
            print(f'Niestety skrzynia jest zamknięta.')
            print(f'Czy chcesz użyć wytrychu do jej otwarcia?')
            choice = input('\nT/N   >')
            if choice == 'n':
                print('\nSkrzynia pozostaje zamknięta.')
                return
            elif choice == 't':
                functions.player.inventory.remove("Lockpick")
                self.opened = True
                functions.player.money += self.gold
                functions.player.inventory.append(self.item)
                functions.player.experience += self.exp
                self.searched = True
                print(f'\nCzy skrzynia otwarta? - {self.opened}\n')
                print(f'Czy była pułapka? - {self.trap}')
                print(f'Czy była zagadka? - {self.puzzle}')
                print(f'Znalezione złoto - {self.gold}')
                print(f'Znalezione przedmioty - {self.item}')
                print(f'Zdobyte doświadczenie - {self.exp}')
                print(f'Czy skrzynia przeszukana? - {self.searched}')
            else:
                print("\nBłędny wybór!")
                input()
                open(self)