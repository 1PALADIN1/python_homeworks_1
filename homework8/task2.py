"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if num2 == 0:
        raise DivByZeroException("На ноль делить нельзя!")

    print(f"Результат деления: {num1 / num2}")
except DivByZeroException as err:
    print(err)
finally:
    print("Конец программы")
