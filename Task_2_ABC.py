from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption_coat(self):
        """Coat method"""

    @abstractmethod
    def fabric_consumption_suit(self):
        """Suit method"""


class Coat(Cloth):
    def __init__(self, name, v):
        super().__init__(name)
        self.size = v

    def __str__(self):
        return f'Size of {self.name} - {self.size}'

    @property
    def fabric_consumption_coat(self):
        return f'To make a {self.name} you need {self.size / 6.5 + 0.5:.2f} m. of cloth'

    def fabric_consumption_suit(self):
        return f'This method is for the Suit only'


class Suit(Cloth):
    def __init__(self, name, h):
        super().__init__(name)
        self.height = h

    def __str__(self):
        return f'Size (height) of {self.name} - {self.height}'

    def fabric_consumption_coat(self):
        return f'This method is for the Coat only'

    @property
    def fabric_consumption_suit(self):
        return f'To make a {self.name} you need {2 * (self.height / 100) + 0.3:.2f} m. of cloth'


c = Coat('Coat', 46)
print(c)
print(c.fabric_consumption_coat)
# print(c.fabric_consumption_suit())
print('-' * 100)
s = Suit('Suit', 170)
print(s)
print(s.fabric_consumption_suit)
# print(s.fabric_consumption_coat())
