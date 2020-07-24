from abc import ABC, abstractmethod


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    type_ = 'Основной класс Склад'
    storage_db = {}  # база данных склада

    @staticmethod
    def add_several_to_storage(equipment):
        """ Метод для добавления группы товаров на склад """
        for unit in equipment:
            try:
                unit.amount = int(unit.amount)
                if unit.name in Storage.storage_db:
                    Storage.storage_db[unit.name] = unit.amount + unit.amount
                else:
                    Storage.storage_db[unit.name] = unit.amount
            except TypeError:
                print('Неправильное значение')
            except ValueError:
                print('Неправильное значение')
        print(f'На складе: {Storage.storage_db}')

    @staticmethod
    def add_single_to_storage(equipment):
        """ Метод для добавления одного товара на склад """
        try:
            equipment.amount = int(equipment.amount)
            if equipment in Storage.storage_db:
                Storage.storage_db[equipment.name] = equipment.amount + equipment.amount
            else:
                Storage.storage_db[equipment.name] = equipment.amount
        except TypeError:
            print('Неправильное значение')
        except ValueError:
            print('Неправильное значение')
        print(f'На складе: {Storage.storage_db}')

    @staticmethod
    def transfer(unit, amount_to_transfer, department):
        """ Метод перемещения товара в подразделение компании """
        if unit.name in Storage.storage_db:
            try:
                if Storage.storage_db[unit.name] <= 0:
                    raise OwnError('На складе не хватает товара')
                Storage.storage_db[unit.name] -= amount_to_transfer
                print(f'Товар {unit.type_eq} {unit.name} перемещен в |{department}|\n'
                      f'В количестве {amount_to_transfer} шт.\nОстаток на складе: {Storage.storage_db}')
            except NameError:
                print('Введено неправильное значение')
            except TypeError:
                print('Введено неправильное значение')
            except OwnError as err:
                print(err)
        else:
            print('Такого товара нет на складе')

    @classmethod
    def type_of_class(cls):
        return cls.type_


class OfficeEquipment(ABC):
    def __init__(self, name, amount, type_eq):
        self.name = name
        self.amount = amount
        self.type_eq = type_eq

    @abstractmethod
    def info(self):
        return f'{self.name}, {self.amount}, {self.type_eq}'


class Printer(OfficeEquipment):
    def __init__(self, name, amount, type_eq):
        super().__init__(name, amount, type_eq)

    def __str__(self):
        return f'По накладной:\nТип: принтер\nМодель: {self.name}\nКоличество: {self.amount}\n{"-" * 100}'

    @property
    def info(self):
        return f'{self.name}, {self.amount}, {self.type_eq}'


class Scanner(OfficeEquipment):
    def __init__(self, name, amount, type_eq):
        super().__init__(name, amount, type_eq)

    def __str__(self):
        return f'По накладной:\nТип: сканнер\nМодель: {self.name}\nКоличество: {self.amount}\n{"-" * 100}'

    @property
    def info(self):
        return f'{self.name}, {self.amount}, {self.type_eq}'


class Xerox(OfficeEquipment):
    def __init__(self, name, amount, type_eq):
        super().__init__(name, amount, type_eq)

    def __str__(self):
        return f'По накладной:\nТип: ксерокс\nМодель: {self.name}\nКоличество: {self.amount}\n{"-" * 100}'

    @property
    def info(self):
        return f'{self.name}, {self.amount}, {self.type_eq}'


printer = Printer('Canon', 3, 'принтер')
print(printer)
scanner = Scanner('Long', 2, 'сканнер')
print(scanner)
xerox = Xerox('Xerox', 1, 'ксерокс')
print(xerox.info)  # обращение к property
print(xerox)
xerox_1 = Xerox('Xerox', 1, 'ксерокс')
xerox_2 = Xerox('Studio', 2, 'ксерокс')  # Такого товара нет на складе

storage = Storage()
storage.add_several_to_storage([printer, scanner, xerox, xerox_1])

storage.transfer(xerox_1, 1, 'Отдел продаж')
storage.transfer(xerox_2, 1, 'Отдел маркетинга')

printer_1 = Printer('SuperPrinter', 5, 'принтер')
storage.add_single_to_storage(printer_1)
print('-' * 100)
print(storage.type_of_class())
