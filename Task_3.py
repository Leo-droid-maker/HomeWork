class OwnException(Exception):
    def __init__(self, text):
        pass


result = []


def get_list():
    while True:
        user_data = input('Введите целые числа через пробел. Для завершения, наберите "stop": ').split()
        try:
            for el in user_data:
                if el != 'stop':
                    try:
                        el = int(el)
                        result.append(el)
                    except ValueError:
                        try:
                            el = float(el)
                            result.append(el)
                        except ValueError:
                            raise OwnException('Неправильное значение!')
                elif el == 'stop':
                    return result
        except OwnException as err:
            print(err)
        print(result)


print(get_list())
