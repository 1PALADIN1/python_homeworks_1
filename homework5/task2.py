# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import os

with open(os.path.join("files", "file2.txt"), "r") as f:
    lines = f.readlines()
    words_count = [len(el.split()) for el in lines]

    print(f"Количество строк: {len(lines)}\nКоличество слов в строках:")
    for index, el in enumerate(words_count):
        print(f"Строка {index + 1}: количество слов - {el}")
