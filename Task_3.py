class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f"Доход сотрудника: {self._income.get('wage') + self._income.get('bonus')} руб."


worker_a = Position('Максим', 'Великолепный', 'Менеджер', 200000, 50000)
worker_b = Position('Alex', 'Stonewood', 'Driver', 25000, 5000)

print(worker_a.get_full_name())
print(worker_a.get_total_income())
print(worker_b.get_full_name())
print(worker_b.get_total_income())
