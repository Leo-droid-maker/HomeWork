import re
from functools import reduce


with open('BASE.txt', 'r') as f:
    list_of_workers = f.readlines()
    names_of_workers = []
    for worker in list_of_workers:
        temp = worker.split()
        if float(temp[1]) < 20000.00:
            names_of_workers.append(temp[0])
    if not names_of_workers:
        print('Сотрудников с окладом меньше 20000.00 руб в данной базе нет')
    else:
        print(f'Сотрудников с окладом меньше 20000.00 руб в данной базе: {len(names_of_workers)} чел.:\n'
              f'{names_of_workers}')


n_list = []
with open('BASE.txt', 'r') as f:
    for line in f:
        num_of_average = re.findall(r'\d*\.\d+|\d+', line)
        nums = [float(i) for i in num_of_average]
        n_list.append(nums)
    temp_list = reduce(lambda x, y: x + y, n_list)
    sum_of_salary = sum(temp_list)
    average_salary = sum_of_salary / len(list_of_workers)
    print(f'Средняя величина дохода сотрудников: {average_salary:.2f} руб')
