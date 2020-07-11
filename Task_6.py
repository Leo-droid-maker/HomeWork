import re

list_of_keys = []
list_of_values = []

with open('Disciplines.txt', 'r', encoding='utf-8') as f:
    disciplines_list = f.readlines()
    for discipline in disciplines_list:
        split_list = discipline.split(':')
        list_of_keys.append(split_list[0])
        nums = re.findall(r'\d+', split_list[1])
        sum_of_nums = sum(map(int, [int(i) for i in nums]))
        list_of_values.append(sum_of_nums)
        result = dict(zip(list_of_keys, list_of_values))

    print(result)
