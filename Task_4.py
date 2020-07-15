from random import randint


class Car:
    def __init__(self, color, name):
        self.speed = randint(50, 200)
        self.color = color
        self.name = name
        self.is_police = False

    def __str__(self):
        return f'Марка {self.name}\nЦвет {self.color}\nСкорость {self.speed}\nПолиция? {self.is_police}.'

    def go(self):
        return f'{self.color} автомобиль {self.name} движется со скоростью {self.speed} км/ч.'

    def stop(self):
        return f'{self.color} автомобиль {self.name} прекратил движение.'

    def turn(self, direction):
        return f'{self.color} автомобиль {self.name} поворачивает {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль превысил разрешенную скорость'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 120:
            return f'Автомобиль превысил разрешенную скорость'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль превысил разрешенную скорость'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль превысил разрешенную скорость, но преследует нарушителя'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


a = Car('красный', 'Mazda')
b = TownCar('синий', 'Toyota')
c = PoliceCar('черно-белый', 'Renault')
d = WorkCar('красный', 'Fiat')
e = SportCar('жёлтый', 'Lamborgini')

print(a)
print(b)
print(c)
print(d)
print(e)
print('=' * 100)
print(b.go())
print(d.turn('налево'))
print(c.show_speed())
print(e.stop())


