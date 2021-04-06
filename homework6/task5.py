"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print(f"[{self.__title}]: Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print("Рисует круг")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        super().draw()
        print("Рисует человека, скетч")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print("Рисует милого котика в стиле аниме")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
