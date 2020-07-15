class Stationery:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.type = 'Шариковая ручка'

    def draw(self):
        return f'Жанр картины {self.title}, используется инструмент {self.type}.'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.type = 'Карандаш'

    def draw(self):
        return f'Жанр картины {self.title}, используется инструмент {self.type}.'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.type = 'Маркер'

    def draw(self):
        return f'Жанр картины {self.title}, используется инструмент {self.type}.'


draw_process = Stationery('')
draw_with_pen = Pen('Портрет')
draw_with_pencil = Pencil('Натюрморт')
draw_with_handle = Handle('Мультяшка')


print(draw_process.draw())
print(draw_with_pen.draw())
print(draw_with_pencil.draw())
print(draw_with_handle.draw())
