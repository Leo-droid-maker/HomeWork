def int_func(text):
    return text.title()

# ------- ПЕРВЫЙ СПОСОБ--------------------------
# БЕЗ ПРОВЕРКИ EN-RU


def get_title(some_text, func):
    s_list = some_text.split()
    total_list = []
    for i in s_list:
        res = func(i)
        total_list.append(res)
    return ' '.join(total_list)


# ------ ВТОРОЙ СПОСОБ ---------------------------------------------

def new_func(some_text, func):
    new_list = some_text.split()
    temp_list = []
    for i in some_text:
        temp_i = ord(i)
        if temp_i >= 1040:
            return 'ERROR'
    for el in new_list:
        temp_res = func(el)
        temp_list.append(temp_res)
    return ' '.join(temp_list)


user_text = input('Enter some words with spaces: ')
user_text_2 = input('Enter another words with spaces: ')
print(get_title(user_text, int_func))
print(new_func(user_text_2, int_func))
