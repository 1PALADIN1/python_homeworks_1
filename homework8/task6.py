"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

from abc import ABC


# region Custom Exceptions

class NotEnoughEqOnStoreException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotCorrectInputException(Exception):
    def __init__(self, message):
        super().__init__(message)

# endregion


# region Core

class Utils:
    @staticmethod
    def is_digit(check_str):
        if check_str[0] in ("-", "+"):
            return check_str[1:].isdigit()

        return check_str.isdigit()


class Store:
    @property
    def name(self):
        return self.__name

    def __init__(self, name):
        self.__name = name
        self.__stored_eq = {}
        self.__released_eq = {}

    # принять на склад
    def accept(self, office_eq, val):
        stored_val = self.__stored_eq.get(office_eq.name)
        if stored_val is not None:
            val += stored_val

        self.__stored_eq.update({office_eq.name: val})

    # передача в подразделение
    def release(self, office_eq, div_name, req_num):
        stored_val = self.__stored_eq.get(office_eq.name)
        if stored_val is None or stored_val - req_num < 0:
            raise NotEnoughEqOnStoreException(f"На складе нет необходимого числа техники {office_eq.name}!")

        self.__stored_eq.update({office_eq.name: stored_val - req_num})
        released_val = self.__released_eq.get(div_name)
        if released_val is not None:
            req_num += released_val

        self.__released_eq.update({div_name: req_num})

    def __str__(self):
        result = f"Состояние склада:\n===== {self.__name} =====\n"
        for el in self.__stored_eq.items():
            result += f"{el[0]}: {el[1]}\n"

        result += "===== RELEASED =====\n"
        released_items = self.__released_eq.items()
        for index, el in enumerate(released_items):
            result += f"{el[0]}: {el[1]}"
            if index < len(released_items) - 1:
                result += "\n"

        return result


class OfficeEquipment(ABC):
    @property
    def name(self):
        return self.__name

    @property
    def paper_amount(self):
        return self.__paper_amount

    @property
    def ink_amount(self):
        return self.__ink_amount

    def __init__(self, name, paper_amount, ink_amount):
        self.__name = name
        self.__paper_amount = paper_amount
        self.__ink_amount = ink_amount

    def use_paper(self, val):
        self.__paper_amount -= val
        if self.__paper_amount < 0:
            self.__paper_amount = 0

    def use_ink(self, val):
        self.__ink_amount -= val
        if self.__ink_amount < 0:
            self.__ink_amount = 0

    def __str__(self):
        return f"[{self.__name}]: paper_amount = {self.__paper_amount}, ink_amount = {self.__ink_amount}"


class PrintType:
    color = 1
    black_and_white = 2


class ScanQuality:
    low = 1
    medium = 2
    high = 3


class Printer(OfficeEquipment):
    @property
    def print_type(self):
        return self.__print_type

    def __init__(self, name, paper_amount, ink_amount, print_type):
        self.__print_type = print_type
        super().__init__(name, paper_amount, ink_amount)


class Scanner(OfficeEquipment):
    @property
    def scan_quality(self):
        return self.__scan_quality

    def __init__(self, name, paper_amount, ink_amount, scan_quality):
        self.__scan_quality = scan_quality
        super().__init__(name, paper_amount, ink_amount)


class Copier(OfficeEquipment):
    @property
    def copies_amount(self):
        return self.__copies_amount

    def __init__(self, name, paper_amount, ink_amount, copies_amount):
        self.__copies_amount = copies_amount
        super().__init__(name, paper_amount, ink_amount)

# endregion


printer = Printer("Printer", 20, 120, PrintType.color)
scanner = Scanner("Scanner", 50, 400, ScanQuality.high)
copier = Copier("Copier", 50, 400, 5)
store = Store("Test Store")
stop_word = "stop"

print(f"Добро пожаловать на склад {store.name}!")

while True:
    input_str = input(f"Что хотите отгрузить?\n"
                      f"1 - принтер\n"
                      f"2 - сканнер\n"
                      f"3 - ксерокс\n"
                      f"Введите нужное число (чтобы завершить шаг, введите {stop_word}):\n")

    if input_str == stop_word:
        break

    try:
        if not Utils.is_digit(input_str):
            raise NotNumberException("Вы указали не число! Повторите попытку")

        val = int(input_str)
        if val not in (1, 2, 3):
            raise NotCorrectInputException("Введёное число не распознанно! Повторите попытку")

        eq_amount = 0
        while True:
            try:
                input_str = input("Сколько техники хотите отгрузить на склад?\n")
                if not Utils.is_digit(input_str):
                    raise NotNumberException("Вы указали не число! Повторите попытку")

                eq_amount = int(input_str)
                if eq_amount <= 0:
                    raise NotCorrectInputException("Количество техники должно быть больше 0! Повторите попытку")
                break
            except NotNumberException as err:
                print(err)
            except NotCorrectInputException as err:
                print(err)

        if val == 1:
            store.accept(printer, eq_amount)
        elif val == 2:
            store.accept(scanner, eq_amount)
        elif val == 3:
            store.accept(copier, eq_amount)

    except NotCorrectInputException as err:
        print(err)
    except NotNumberException as err:
        print(err)

print(store)
