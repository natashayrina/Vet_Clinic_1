# 2)Сделаем словарь для вет клиники. Каждое животное имеет ключ - его кличка и параметры - рост, вес, имя владельца, возраст и тип(кошка/собака/хомяк)
# 2.1)Пользователь вводит тип животного. Вывести всех животных этого типа
# 2.2)Пользователь вводит имя владельца. Вывести всех животных этого владельца
# 2.3)Пользователь вводит возраст - критерий "взрослого животного".
# К каждому животному добавляется поле is_adult, оно равно True если животное взрослое и False иначе
# 2.4)Вывести всех котов с ожирением и присвоить им степень.
# Пользователь вводит число - критерий ожирения.
# Если вес котика превышает это число на 3.5 - это 1 степень ожирения, если на 4.5 - 2я степень, если больше 3-я степень
from Dictionaris import *
from View import *
from Functions import *

main(animals_all)
# get_menu_choice()
# choice = get_menu_choice_of_type_animals()
# new_list_of_type = search_type_of_animal(choice, animals_all)
#  print(new_list_of_type)
# new_list_of_owner = search_owner(animals_all)
#  print (new_list_of_owner)




