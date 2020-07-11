rus_numbers = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Ноль']
count = 0
rus_leng = []
with open('Numbers.txt', 'r', encoding='utf-8') as f:
    list_of_eng = f.readlines()
    for i in list_of_eng:
        split_line = i.split()
        split_line[0] = rus_numbers[count]
        split_line[2] += '\n'
        rus_leng.append(' '.join(split_line))
        count += 1
    # print(rus_leng)

with open('RUS_Numbers.txt', 'w', encoding='utf-8') as f:
    f.writelines(rus_leng)

print('Перевод завершен')




