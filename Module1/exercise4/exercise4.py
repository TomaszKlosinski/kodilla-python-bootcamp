def check_available_cheese(available_cheese):
    if 'edam' in available_cheese:
        print('Edam')
    elif 'brie' in available_cheese:
        print("Brie")
    elif 'gouda' in available_cheese:
        print("Gouda")
    else:
        print("Nie ma sera")


available_cheese = ['edam', 'brie', 'gouda']
check_available_cheese(available_cheese)

available_cheese = ['brie', 'gouda']
check_available_cheese(available_cheese)

available_cheese = ['gouda']
check_available_cheese(available_cheese)

available_cheese = []
check_available_cheese(available_cheese)


