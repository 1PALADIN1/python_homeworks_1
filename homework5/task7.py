"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import os
import json

total_profit = 0
profit_firms = 0
firms_dict = {}
with open(os.path.join("files", "file7.txt"), "r") as f:
    for line in f:
        data = line.split()
        income = float(data[2]) - float(data[3])

        if income >= 0:
            total_profit += income
            profit_firms += 1

        firms_dict.update({data[0]: income})

average_profit = 0
if profit_firms > 0:
    average_profit = total_profit / profit_firms

result = [firms_dict, {"average_profit": average_profit}]

with open(os.path.join("files", "file7_output.txt"), "w") as f:
    json.dump(result, f)

print(f"Json объект записан в файл file7_output.txt. Результат:\n{result}")
