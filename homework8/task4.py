"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

from abc import ABC


class Store:
    def __init__(self, name):
        self.__name = name


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
print(f"{printer}, print type = {printer.print_type}")

scanner = Scanner("Scanner", 50, 400, ScanQuality.high)
print(f"{scanner}, scan quality = {scanner.scan_quality}")

copier = Copier("Copier", 50, 400, 5)
print(f"{copier}, number of copies = {copier.copies_amount}")

copier.use_ink(250)
print(copier)
copier.use_paper(40)
print(copier)
