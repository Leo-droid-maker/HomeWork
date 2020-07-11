with open('SumOfNumb.txt', 'w', encoding='utf-8') as f:
    f.write(input('Введите числа через пробел: '))

with open('SumOfNumb.txt', 'r', encoding='utf-8') as f:
    try:
        a = f.readlines()
        for num in a:
            digital = num.split()
            print(f'Результат: {sum(map(int, digital))}')
    except ValueError:
        print('Введено неправильное значение.')
