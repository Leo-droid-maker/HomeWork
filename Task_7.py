import json


def difference(some_list):
    diff = some_list[0] - some_list[1]
    return diff


def average_profit(another_list):
    temp = 0
    count = 0
    for i in another_list:
        if i <= 0:
            continue
        elif i > 0:
            temp += i
            count += 1
    av_prof = temp / count
    return av_prof


list_of_firms = []
list_of_profit = []

with open('FirmSpisok.txt', 'r', encoding='utf-8') as f:
    get_list = f.readlines()
    for firm in get_list:
        split_list = firm.split()
        list_of_firms.append(split_list[0])
        dig = list(map(int, split_list[2:]))
        profit = difference(dig)
        list_of_profit.append(profit)
        first_dict = dict(zip(list_of_firms, list_of_profit))
    second_dict = {'average profit': average_profit(list_of_profit)}

total_result = [first_dict, second_dict]
# print(total_result)


with open('FirmDB.json', 'w', encoding='utf-8') as f:
    json.dump(total_result, f, ensure_ascii=False)


with open('FirmDB.json', 'r', encoding='utf-8') as js:
    file = json.load(js)

print(file)
