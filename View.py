from Functions import *

look_for_type_of_animal = 1
look_for_owner = 2
look_for_age = 3
quit = 4
def get_menu_choice():
    print("1. Найти животное по его типу")
    print("2. Найти животное по его владельцу")
    print("3. Найти пожилых или молодых животных")
    print("4. Закончить работу")
    print()
    choice = int(input("Введите выбранный пункт: "))

    return choice


def get_menu_choice_of_type_animals():
    print("1. Собака")
    print("2. Кошка")
    print("3. Попугай")
    print("4. Морская свинка")
    print("5. Кролик")
    print("6. Выход")
    print()
    need_type = input("Какой тип животного Вас интересует?")
    return need_type

def get_name_of_owner():
    owner = input("Введите имя владельца: ")
    return owner

def print_of_animal(animals_list):
    for elem in animals_list:
        print (elem)