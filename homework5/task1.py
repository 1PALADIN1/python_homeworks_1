# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

import os

f = open(os.path.join("files", "file1.txt"), "w")
while True:
    input_data = input("Введите строку:\n")
    if input_data == "":
        break

    f.write(f"{input_data}\n")

if not f.closed:
    f.close()
