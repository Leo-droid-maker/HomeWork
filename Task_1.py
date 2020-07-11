with open('test.txt', 'w', encoding='utf-8') as f:
    print('Ваши данные будут записаны построчно в файл test.txt\nДля завершения записи нажмите Enter ничего не вводя.')
    while True:
        content = input('Введите данные: ')
        line = f.write(content + '\n')
        if not content:
            break
