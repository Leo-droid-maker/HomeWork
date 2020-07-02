number_of_goods = int(input('Сколько видов товаров Вам нужно?: '))

per_list = []
dict_of_goods = {}
analysis = {}
name_of_goods = []
price_of_goods = []
amount_of_goods = []
unit = set()

for i in range(number_of_goods):
    # Заполняю словарь
    dict_of_goods['название'] = input('Введите название товара: ')
    dict_of_goods['цена'] = int(input('Введите цену товара: '))
    dict_of_goods['количество'] = int(input('Введите количество: '))
    dict_of_goods['ед'] = input('Единица измерения: ')
    # Заполняю список словарей
    per_list.append(dict_of_goods)
    # Заполняю списки для аналитики
    name_of_goods.append(dict_of_goods.get('название'))
    price_of_goods.append(dict_of_goods.get('цена'))
    amount_of_goods.append(dict_of_goods.get('количество'))
    unit.add(dict_of_goods.get('ед'))


data_base = list(enumerate(per_list, 1))
analysis['название'] = name_of_goods
analysis['цена'] = price_of_goods
analysis['количество'] = amount_of_goods
analysis['ед'] = list(unit)

print(f'Структура данных: {data_base}')
print(f'Аналитика: {analysis}')


