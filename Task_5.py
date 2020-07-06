def if_q_in_list(some_list):
    result = 0
    for i in some_list:
        if i == 'q' or i == 'Q':
            break
        else:
            result += int(i)
    return result


def my_sum(some_list):
    temp = []
    sum_of_list = sum(map(int, some_list))
    temp.append(sum_of_list)
    result_sum = sum(temp)
    return result_sum


def total_sum(func_1, func_2):
    result = 0
    while True:
        try:
            total_list = input('Введите числа: ').split()
            if 'q' in total_list:
                result += func_1(total_list)
                break
            else:
                result += func_2(total_list)
                print(f'Результат: {result}')
        except ValueError:
            print('Неправильное значение!\nНажмите Enter чтобы увидеть текущий результат.')
            continue
    return result


print('Добро пожаловать в счетную программу!\nПросто вводите числа через пробел.\n'
      'Чтобы завершить программу, наберите q')
print(total_sum(if_q_in_list, my_sum))

