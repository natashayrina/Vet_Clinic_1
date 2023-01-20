animal_1 = {'type': 'собака', 'name': 'Дарт', 'date_of_birth': 2022, 'growth': 55, 'weight': 23,
            'owner': 'Шаурина Наталья Сергеевна'}
animal_2 = {'type': 'собака', 'name': 'Дюша', 'date_of_birth': 2010, 'growth': 20, 'weight': 3,
            'owner': 'Шаурина Наталья Сергеевна'}
animal_3 = {'type': 'кошка', 'name': 'Лексус', 'date_of_birth': 2016, 'growth': 30, 'weight': 6,
            'owner': 'Шаурина Наталья Сергеевна'}
animal_4 = {'type': 'собака', 'name': 'Мартин', 'date_of_birth': 2020, 'growth': 30, 'weight': 18,
            'owner': 'Ковалев Константин Александрович'}
animal_5 = {'type': 'кошка', 'name': 'Марс', 'date_of_birth': 2012, 'growth': 25, 'weight': 8,
            'owner': 'Ковалев Константин Александрович'}
animal_6 = {'type': 'морская свинка', 'name': 'Кузя', 'date_of_birth': 2019, 'growth': 10, 'weight': 0.7,
            'owner': 'Демина Ольга Евгеньевна'}
animal_7 = {'type': 'кролик', 'name': 'Дадли', 'date_of_birth': 2018, 'growth': 30, 'weight': 4,
            'owner': 'Саврушева Ольга Эрнестовна'}
animal_8 = {'type': 'собака', 'name': 'Лика', 'date_of_birth': 2019, 'growth': 60, 'weight': 27,
            'owner': 'Деркачева Татьяна Васильевна'}
animal_9 = {'type': 'собака', 'name': 'Бруно', 'date_of_birth': 2015, 'growth': 40, 'weight': 20,
            'owner': 'Деркачева Татьяна Васильевна'}
animal_10 = {'type': 'кошка', 'name': 'Муся', 'date_of_birth': 2016, 'growth': 25, 'weight': 5,
             'owner': 'Деркачева Татьяна Васильевна'}
animal_11 = {'type': 'попугай', 'name': 'Кеша', 'date_of_birth': 2022, 'growth': 9, 'weight': 0.2,
             'owner': 'Деркачева Татьяна Васильевна'}
animal_12 = {'type': 'морская свинка', 'name': 'Хома', 'date_of_birth': 2019, 'growth': 12, 'weight': 3.5,
             'owner': 'Деркачева Татьяна Васильевна'}
animal_13 = {'type': 'попугай', 'name': 'Рома', 'date_of_birth': 2020, 'growth': 11, 'weight': 0.3,
             'owner': 'Егорова Любовь Никитична'}
animal_14 = {'type': 'кошка', 'name': 'Варя', 'date_of_birth': 2017, 'growth': 35, 'weight': 7,
             'owner': 'Егорова Любовь Никитична'}
animal_15 = {'type': 'кролик', 'name': 'Филя', 'date_of_birth': 2018, 'growth': 25, 'weight': 5,
             'owner': 'Киселев Павел Сергеевич'}
animals_all = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10,
               animal_11, animal_12, animal_13, animal_14,
               animal_15]

for elem in animals_all:
    elem['is_adult'] = 'False'

    if elem ['date_of_birth'] <=2020:
        elem['is_adult'] = 'True'
print(animals_all)