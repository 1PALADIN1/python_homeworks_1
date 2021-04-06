"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self.__color = color
        self._name = name
        self.__is_police = is_police

    def go(self):
        print(f"[{self._name}]: Машина отправилась в путь")
        self.__print_car_info()

    def stop(self):
        print(f"[{self._name}]: Машина остановилась")

    def turn(self, direction):
        print(f"[{self._name}]: Машина изменила направление. Текущее значение: {direction}")

    def show_speed(self):
        print(f"[{self._name}]: Скорость: {self._speed}")

    def __print_car_info(self):
        print(f"[{self._name}]: Цвет - {self.__color}, текущая скорость - {self._speed}, полицейская машина? "
              f"- {self.__is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()

        if self._speed > 60:
            print(f"[{self._name}]: Обнаружено превышение скорости!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()

        if self._speed > 40:
            print(f"[{self._name}]: Обнаружено превышение скорости!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# TownCar
tc = TownCar(40, "Синий", "Lada")
tc.go()
tc.turn("Лево")
tc.show_speed()
tc.stop()

tc = TownCar(64, "Фиолетовый", "Mercedes")
tc.go()
tc.show_speed()
tc.stop()

# SportCar
sc = SportCar(450, "Красный", "Lamborghini")
sc.go()
sc.show_speed()
sc.stop()

# WorkCar
wc = WorkCar(20, "Чёрный", "Citroen")
wc.go()
wc.show_speed()
wc.turn("Северо-восток")
wc.stop()

wc = WorkCar(89, "Чёрный", "Citroen")
wc.go()
wc.show_speed()
wc.stop()

# PoliceCar
pc = PoliceCar(120, "Белый", "Skoda")
pc.go()
pc.show_speed()
pc.turn("Назад")
pc.stop()
