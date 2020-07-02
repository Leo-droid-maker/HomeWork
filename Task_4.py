user_word = input('Введите слова через пробел: ')
list_of_words = user_word.split()
res = []

for i in list_of_words:
    if len(i) < 10:
        res.append(i)
    elif len(i) >= 10:
        i = i[:10]
        res.append(i)

for i, el in enumerate(res, 1):
    print(i, el)
