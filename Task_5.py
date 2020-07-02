my_list = [7, 5, 3, 3, 2]
print(f'Наш текущий рейтинг: {my_list}')
num = int(input('Введите новое значение рейтинга: '))

for el in range(len(my_list)):
    if num > my_list[0]:
        my_list.insert(0, num)
        break
    elif num < my_list[-1]:
        my_list.append(num)
        break
    elif my_list[el - 1] == num == my_list[el]:
        my_list.insert(el + 1, num)
        break
    elif my_list[el + 1] < num < my_list[el]:
        my_list.insert(el + 1, num)
        break
    else:
        continue

print(f'Новый рейтинг: {my_list}')
