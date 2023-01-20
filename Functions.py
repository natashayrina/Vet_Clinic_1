from View import *
from Dictionaris import *


def main(animals_all):
    choice: int = 0
    while choice != quit:
        var = choice == get_menu_choice()
        if choice == look_for_type_of_animal:
            result = search_type_of_animal(choice, animals_all)

        elif choice == look_for_owner:
            result = search_owner(animals_all)

        elif choice == look_for_age:
            result = search_age(ages, animals_all)

        print_of_animal(result)


def get_need_type():
    need_type = 0
    while need_type != quit:
        need_type = get_menu_choice_of_type_animals()
        search_type_of_animal(animals_all)


def search_type_of_animal(need_type, animals_all):
    list_of_type = []
    for elem in animals_all:
        if elem['type'] == need_type:
            list_of_type.append(elem)

    return list_of_type

def search_owner(animals_all):
    owner_list = []
    owner = get_name_of_owner()
    for elem in animals_all:
        if elem['owner'] == owner:
            owner_list. append(elem)
    return owner_list

def search_age(ages, animals_all):
    ages = get_adult()
    for elem in animals_all:
        if ages == elem ['is_adult' :'True']:
            print("Животное взрослое")
        else:
            print("Животное еще молодое")




