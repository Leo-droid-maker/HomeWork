# Первый вариант:
def get_degree(num_1, num_2):
    count = 1
    temp = num_1
    res = 0
    if num_2 < 0:
        num_2 = abs(num_2)
        while count < num_2:
            temp *= num_1
            res = 1 / temp
            count += 1
        return f'Ваш результат: {res}'
    elif num_2 > 0:
        while count < num_2:
            temp *= num_1
            count += 1
        return f'Ваш результат: {temp}'


print('Программа возведения числа в степень.')
while True:
    try:
        a = float(input('Введите вещественное число: '))
        b = int(input('Введите степень: '))
        print(get_degree(a, b))
        break
    except ValueError:
        print('Ой всё!')
        continue


# Второй вариант:

def get_degree(num_1, num_2):
    res = num_1 ** num_2
    return f'Результат: {res:.3f}'


print('Введите два числа')
a = float(input('Введите вещественное число: '))
b = int(input('Введите отрицательное число: '))

print(get_degree(a, b))
