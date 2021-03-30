# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def mul_values(value1, value2):
    return value1 * value2


result = reduce(mul_values, [el for el in range(100, 1001)])
print(result)

# вариант с лямбдой
result = reduce(lambda x, y: x * y, [el for el in range(100, 1001)])
print(result)
