
class Coat:
    def __init__(self, v):
        self.size_of_coat = v / 6.5 + 0.5

    def __str__(self):
        return f'Необходимое количество ткани для пошива пальто: {self.size_of_coat:.2f}'


class Suit:
    def __init__(self, h):
        self.height_of_suit = 2 * (h / 100) + 0.3

    def __str__(self):
        return f'Необходимое количество ткани для пошива костюма: {self.height_of_suit:.2f}'


class Cloth:
    def __init__(self, name):
        self.name = name
        self.total = []

    def add_coat(self, v):
        self.total.append(Coat(v).size_of_coat)

    def add_suit(self, h):
        self.total.append(Suit(h).height_of_suit)

    @property
    def result(self):
        res = sum(self.total)
        return f'Общее количество ткани (тип {self.name}): {res:.2f} м.'


b = Suit(170)
print(b)

c = Coat(46)
print(c)

a = Cloth('шерсть')
a.add_coat(46)
a.add_suit(170)
print(a.result)


