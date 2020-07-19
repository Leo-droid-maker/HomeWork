class Matrix:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.num]))

    def __add__(self, other):
        return Matrix([[x + y for x, y in zip(i[0], i[1])] for i in zip(self.num, other.num)])


a = Matrix([[1, -2, 3], [4, 5, -6], [7, 8, -9]])
b = Matrix([[10, 20, -30], [-40, 50, 60], [70, 80, 90]])

print(a)
print('-' * 100)
print(b)
print('-' * 100)
print(a + b)
