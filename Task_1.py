from sys import argv


def get_salary(hours, rate, award):
    result = float((hours * rate) + award)
    print('=' * 50)
    print(f'Заработная плата сотрудника: {result:.2f}')


print('Для расчета З/П сотрудника, введите сл. параметры ЧЕРЕЗ ПРОБЕЛ:\n"start" - для запуска программы,\n'
      'Кол-во отработанных часов\nРазмер ставки\nПремия')

try:
    command = argv[1]

    if command == 'start':
        try:
            w_hours = float(argv[2])
            w_rate = float(argv[3])
            w_award = float(argv[4])
            get_salary(w_hours, w_rate, w_award)
        except ValueError:
            print('=' * 50)
            print('Введен некорректный параметр')
        except IndexError:
            print('*' * 50)
            print('Не введены параметры расчета')
    else:
        print('*' * 50)
        print('Неправильно указан параметр "start"')
except IndexError:
    print('=' * 50)
    print('Начните работу, вводя параметры')
