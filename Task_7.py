class ComplexNumber:
    def __init__(self, x):
        self.x = complex(x)

    def __str__(self):
        return f'{self.x}'

    def __add__(self, other):
        return ComplexNumber(self.x + other.x)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x)


s = ComplexNumber(1 + 2j)
a = ComplexNumber(3 + 4j)
d = s + a
e = s * a
print(s)
print(a)
print(d)
print(e)
