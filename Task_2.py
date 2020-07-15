class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def __str__(self):
        return f'Ширина дорожного полотна: {self._length}, Длина: {self._width}'

    def find_mass(self, mass_of_asphalt, thickness):
        return f'Масса асфальта, необходимого для покрытия дорожного полотна\nШириной {self._length} м.\n' \
               f'Длиной {self._width} м.\nПри массе на кв.метр {mass_of_asphalt} кг. и толщине {thickness} см.\n' \
               f'Равна: {(self._length * self._width * mass_of_asphalt * thickness) // 1000} т.'


a = Road(20, 5000)
print(a)

print(a.find_mass(25, 5))
