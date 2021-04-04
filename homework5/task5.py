"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os
import random


def generate_numbers():
    with open(os.path.join("files", "file5.txt"), "w") as f:
        for i in range(0, 1000):
            f.write(f"{random.randrange(0, 1000)} ")


def calc_numbers():
    with open(os.path.join("files", "file5.txt"), "r") as f:
        nums = f.readline().split()

        result = 0
        for num in nums:
            result += float(num)
        print(f"Сумма чисел в файле: {result}")


generate_numbers()
calc_numbers()
