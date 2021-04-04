"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname} ({self.position})"

    def get_total_income(self):
        income = self._income
        return income.get("wage") + income.get("bonus")


p = Position("Виктор", "Степанов", "Бухгалтер", {"wage": 50000, "bonus": 2000})
print(p.get_full_name())
print(p.get_total_income())

p = Position("Анастасия", "Глухарь", "Прораммист", {"wage": 120000, "bonus": 8900})
print(p.get_full_name())
print(p.get_total_income())
