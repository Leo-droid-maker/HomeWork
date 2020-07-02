number = int(input('Введите номер интересующего месяца от 1 до 12: '))

# Через СПИСОК №1
# Коротко, но запутано, тк список сезонов можно случайно нарушить
list_of_season = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn',
                  'Autumn', 'Winter']
result = list_of_season[number - 1]
print(f'The season is: {result}')

# ===================================================================================================================
# Через СПИСОК №2
list_of_season = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    if number == 12 or number == 1 or number == 2:
        print(f'Время года этого месяца: {list_of_season[0]}')
        break
    elif number == 3 or number == 4 or number == 5:
        print(f'Время года этого месяца: {list_of_season[1]}')
        break
    elif number == 6 or number == 7 or number == 8:
        print(f'Время года этого месяца: {list_of_season[2]}')
        break
    elif number == 9 or number == 10 or number == 11:
        print(f'Время года этого месяца: {list_of_season[3]}')
        break
    else:
        number = int(input('Введите номер интересующего месяца от 1 до 12: '))

# ===================================================================================================================

# Через СЛОВАРЬ
dict_of_season = {
    12: 'Зима',
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень'
}

# Попробовал использовать тернарный оператор, но не знаю, можно ли его использовать с f строками ?
# И почему возвращает None ?
# print(dict_of_season[number] if number else print('Вы ввели не правильное значение. Повторите попытку'))
#
while True:
    if number in dict_of_season:
        if number:
            print(f'Время года: {dict_of_season[number]}')
            break
    else:
        number = int(input('Введите номер интересующего месяца: '))
