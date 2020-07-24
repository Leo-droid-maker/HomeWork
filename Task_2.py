class OwnDivisionError(Exception):
    def __init__(self, text):
        self.text = text


first_dig = int(input('Введите первое число: '))
second_dig = int(input('Введите второе число: '))
try:
    if second_dig == 0:
        raise OwnDivisionError('Невозможно поделить на ноль!')
except ValueError:
    print('Вы не ввели данные')
except OwnDivisionError as err:
    print(err)
else:
    result = first_dig / second_dig
    print(f'Ваш результат: {result:.1f}')



