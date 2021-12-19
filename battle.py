import time
from temp import clear_screen

clear_screen()
hero_name = input('\nPodaj swoje imię: ')
print(f'\n\nWitaj, {hero_name.title()}\n\n')
time.sleep(1)
print(f'\n\nRozpoczyna się walka z Goblinem!')
time.sleep(1)