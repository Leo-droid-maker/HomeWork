def division(first_dig, sec_dig):
    try:
        res = first_dig / sec_dig
        return f'Результат деления: {res:.1f}'
    except ZeroDivisionError:
        return f'Попытка деления на ноль.'


print("Введите два числа для деления")
a = int(input("Введите первое число: "))
b = int(input('Введите второе число: '))
print(division(a, b))
