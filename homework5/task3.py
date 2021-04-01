# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import os

with open(os.path.join("files", "file3.txt"), "r") as f:
    lines = f.readlines()

    total_sum = 0
    print(">>> Сотрудники, оклад которых меньше 20 тыс.:")
    for el in lines:
        pair = el.split()
        employee = pair[0]
        income = float(pair[1])
        total_sum += income

        if income < 20000:
            print(f"{employee} - {income}")

    print(f">>> Средний оклад: {total_sum / len(lines)}")
