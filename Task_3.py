class Cell:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'{self.x}'

    def __add__(self, other):
        return f'Клетки подружились и образовали новую с общим количеством: {Cell(self.x + other.x)} клеток'

    def __sub__(self, other):
        if (self.x - other.x) > 0:
            return f'На клетки напал вирус и оставил всего: {Cell(self.x - other.x)} клеток'
        else:
            return f'Вирус напал на тестируемые клетки и сожрал их все,\n' \
                   f'произведите сложение клеток для их восстановления'

    def __mul__(self, other):
        return f'Клеточки очень сильно любят друг друга. Новое количество: {Cell(self.x * other.x)} клеток'

    def __truediv__(self, other):
        if isinstance((self.x / other.x), float):
            return f'Клетки не способны разделиться таким образом'

    def __floordiv__(self, other):
        return f'Клетки поссорились и разделились. Осталось всего: {Cell(self.x // other.x)} клеток'

    def make_order(self, r):
        print(f'количество ячеек в ряду: {r}, приобщем кол-ве {self.x}')
        temp = self.x // r
        temp2 = self.x % r
        count = 0
        if temp % 2 == 0:
            for i in range(self.x + temp):
                if count < r:
                    print('*', end='')
                    count += 1
                elif count == r:
                    print()
                    count = 0
                    continue
        else:
            for i in range(self.x + temp2 + 2):
                if count < r:
                    print('*', end='')
                    count += 1
                elif count == r:
                    print()
                    count = 0
                    continue


a = Cell(12)
b = Cell(2)
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
print(c)
print(d)
print(e)
print(f)
print(g)
a2 = Cell(2)
b2 = Cell(8)
c2 = a2 - b2
print(c2)
print('-' * 100)
a.make_order(5)
