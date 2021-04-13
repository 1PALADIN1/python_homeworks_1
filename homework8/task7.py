"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real, i):
        self.__real = real
        self.__i = i

    def __str__(self):
        if self.__i > 0:
            return f"{self.__real} + {self.__i}i"

        if self.__i < 0:
            return f"{self.__real} - {abs(self.__i)}i"

        return f"{self.__real}"

    def __add__(self, other):
        real = self.__real + other.__real
        i = self.__i + other.__i
        return Complex(real, i)

    def __sub__(self, other):
        real = self.__real - other.__real
        i = self.__i - other.__i
        return Complex(real, i)

    def __mul__(self, other):
        real = self.__real * other.__real - self.__i * other.__i
        i = self.__real * other.__i + self.__i * other.__real
        return Complex(real, i)


num1 = Complex(8, 4)
num2 = Complex(1, -9)
num3 = Complex(-6, 0)

print("Числа:")
print(num1, num2, num3, sep="\n")

print("\nСложение:")
print(f"({num1}) + ({num2}) = {num1 + num2}")
print(f"({num1}) + ({num3}) = {num1 + num3}")
print(f"({num2}) + ({num3}) = {num2 + num3}")
print(f"({num1}) + ({num2}) + ({num3}) = {num1 + num2 + num3}")

print("\nВычитание:")
print(f"({num1}) - ({num2}) = {num1 - num2}")
print(f"({num2}) - ({num3}) = {num2 - num3}")

print("\nУмножение:")
print(f"({num1}) * ({num2}) = {num1 * num2}")
print(f"({num2}) * ({num3}) = {num2 * num3}")
