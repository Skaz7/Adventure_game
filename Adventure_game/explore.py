'''
Module for exploring world, which is build as separated rooms.
Player explores each room and encouters different monsters and traps.
'''


from functions import clear_screen

def explore():
    pass

clear_screen()

def region_builder(region_list, region_name, next_regions):
    print(f'Dotarłeś do {region_name}.')
    region_count = len(region_list)
    choices = []

    input_message = 'Jaką akcję podejmujesz?    > ('

    
