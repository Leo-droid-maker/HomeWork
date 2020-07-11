with open('text.txt', 'r', encoding='utf-8') as f:
    main_list = []
    count = 1
    for line in f:
        main_list.append(line.replace('\n', ''))
    print(f'Количество строк в файле: {len(main_list)}')
    for el in main_list:
        temp_list = el.split()
        print(f'В строке {count} количество слов: {len(temp_list)}')
        count += 1
