"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

from abc import ABC


class Store:
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
            print(f"На складе нет необходимого числа техники {office_eq.name}!")
            return

        self.__stored_eq.update({office_eq.name: stored_val - req_num})
        released_val = self.__released_eq.get(div_name)
        if released_val is not None:
            req_num += released_val

        self.__released_eq.update({div_name: req_num})

    def __str__(self):
        result = f"===== {self.__name} =====\n"
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


printer = Printer("Printer", 20, 120, PrintType.color)
scanner = Scanner("Scanner", 50, 400, ScanQuality.high)
copier = Copier("Copier", 50, 400, 5)

store = Store("Test Store")
store.accept(printer, 10)
store.accept(scanner, 12)
store.accept(scanner, 7)
store.accept(copier, 4)

print(store, "\n")

store.release(printer, "Test division 1", 9)
store.release(printer, "Test division 2", 4)

print(store, "\n")

store.release(scanner, "Test division 3", 15)
store.release(copier, "Test division 4", 4)

print(store, "\n")
