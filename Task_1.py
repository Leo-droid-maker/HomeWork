my_list = [[1, 5], 'some string', 123, {2, 5, 'string'}, 2.5, {'name': 'Max'}, -5, ('str', 'int')]
count = 0

for i in my_list:
    count += 1
    print(f'{count}-й элемент списка имеет тип: {type(i)}')
