"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix: [[]]):
        self.__matrix = matrix

    def __str__(self):
        result = ""
        for row_index, row in enumerate(self.__matrix):
            for col_index, el in enumerate(row):
                if col_index == len(row) - 1:
                    result += f"{el}"
                else:
                    result += f"{el}, "

            if row_index < len(self.__matrix) - 1:
                result += "\n"

        return result

    def __add__(self, other):
        result = []
        for row_index, row in enumerate(self.__matrix):
            new_row = []
            for col_index, el in enumerate(row):
                val = el + other.__matrix[row_index][col_index]
                new_row.append(val)

            result.append(new_row)

        return Matrix(result)


test_matrix1 = [
    [1, 2, 3],
    [4, 6, 5]
]

test_matrix2 = [
    [-9, 21, 133],
    [14, -87, 50]
]

test_matrix3 = [
    [78, 0, -500],
    [-123, 7, 8]
]

m1 = Matrix(test_matrix1)
m2 = Matrix(test_matrix2)
m3 = Matrix(test_matrix3)

print(f"Matrix 1:\n{m1}\n")
print(f"Matrix 2:\n{m2}\n")
print(f"Matrix 3:\n{m3}\n")

sum_matrix = m1 + m2 + m3
print(f"Matrix sum:\n{sum_matrix}")
