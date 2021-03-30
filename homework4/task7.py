# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from functools import reduce


# 1 способ
def fact1(number):
    for el in [reduce(lambda x, y: x * y, range(1, i + 1))
               for i in range(1, number + 1)]:
        yield el


# 2 способ
def fact2(number):
    for i in range(1, number + 1):
        result = 1
        for j in range(1, i + 1):
            result *= j
        yield result


n = 10
for val in fact1(n):
    print(val)

for val in fact2(n):
    print(val)
