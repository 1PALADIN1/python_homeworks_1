# Вторая часть 6-ого задания
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle

test_list = [1, 2, "rer", True, 12.0]

c = 0
for el in cycle(test_list):
    if c > 20:
        break

    print(el)
    c += 1
