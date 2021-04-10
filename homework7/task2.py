"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __str__(self):
        return f"{self.__name}"


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.__v = v

    @property
    def tissue_consumption(self):
        return self.__v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.__h = h

    @property
    def tissue_consumption(self):
        return self.__h * 2 + 0.3


coat = Coat("Test coat", 52)
costume = Costume("Test costume", 180)

print(f"{coat}: {coat.tissue_consumption}")
print(f"{costume}: {costume.tissue_consumption}")
