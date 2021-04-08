"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, number):
        self.__number = number

    def __add__(self, other):
        val = self.__number + other.__number
        return Cell(val)

    def __sub__(self, other):
        val = self.__number - other.__number
        if val <= 0:
            print("Не удалось вычесть клетки")
            return None
        return Cell(val)

    def __mul__(self, other):
        val = self.__number * other.__number
        return Cell(val)

    def __truediv__(self, other):
        val = self.__number // other.__number
        return Cell(val)

    # region Compare
    def __lt__(self, other):
        return self.__number < other.__number

    def __le__(self, other):
        return self.__number <= other.__number

    def __gt__(self, other):
        return self.__number > other.__number

    def __ge__(self, other):
        return self.__number >= other.__number

    def __eq__(self, other):
        return self.__number == other.__number

    def __ne__(self, other):
        return self.__number != other.__number
    # endregion

    def __str__(self):
        return f"Cell[{self.__number}]"

    def make_order(self, number_in_row):
        numbers_left = self.__number

        result = ""
        while numbers_left > 0:
            numbers_left -= number_in_row

            if numbers_left > 0:
                result += self.__create_row(number_in_row) + "\n"
            elif numbers_left == 0:
                result += self.__create_row(number_in_row)
            else:
                result += self.__create_row(number_in_row + numbers_left)

        return result


    def __create_row(self, number_in_row):
        result = ""
        for i in range(number_in_row):
            result += "*"

        return result


cell1 = Cell(15)
cell2 = Cell(20)
cell3 = Cell(4)

# operations tests
print("Операции:")
print(f"{cell1} + {cell2} = {cell1 + cell2}")

sub_test_list = [
    [cell1, cell3],
    [cell1, cell2],
    [cell2, cell3]
]

for el in sub_test_list:
    c1 = el[0]
    c2 = el[1]

    if c1 <= c2:
        print(f"Невозвоможно провести операцию вычитания: {c1} - {c2}")
        continue

    print(f"{c1} - {c2} = {c1 - c2}")

print(f"{cell1} * {cell2} = {cell1 * cell2}")
print(f"{cell1} / {cell2} = {cell1 / cell2}")
print(f"{cell2} / {cell1} = {cell2 / cell1}")
print(f"{cell2} / {cell3} = {cell2 / cell3}")

# make order tests
print("\nПроверка make_order:")

print(f"{cell1}, 3 ячейки:\n{cell1.make_order(3)}")
print(f"{cell1}, 4 ячейки:\n{cell1.make_order(4)}")
print(f"{cell2}, 12 ячеек:\n{cell2.make_order(12)}")
print(f"{cell3}, 2 ячейки:\n{cell3.make_order(2)}")
