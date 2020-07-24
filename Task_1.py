from datetime import date


class Data:

    def __init__(self):
        self.data = '20-06-2020'
        # self.data = '30-02-2020' - Uncorrected data

    def __str__(self):
        return self.data

    @classmethod
    def get_number(cls):
        temp = list(map(int, Data().data.split('-')))
        return f'{int(temp[0])}.{int(temp[1])}.{int(temp[2])}'

    @staticmethod
    def check_data():
        temp = list(map(int, Data().get_number().split('.')))
        try:
            if date(temp[2], temp[1], temp[0]):
                return f'{int(temp[0])}.{int(temp[1])}.{int(temp[2])} - Correct data.'
        except ValueError:
            return 'Uncorrected data'


a = Data()
print(a)
print(a.get_number())
print(a.check_data())

