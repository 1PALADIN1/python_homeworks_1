"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

words_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}


def read_lines_from_file():
    with open(os.path.join("files", "file4.txt"), "r") as f:
        result = f.readlines()
    return result


def write_lines_to_file(input_lines):
    with open(os.path.join("files", "file4_output.txt"), "w") as f:
        for el in input_lines:
            f.write(el)
    print("Результат записан в файл file4_output.txt")


lines = read_lines_from_file()

for index, line in enumerate(lines):
    word = line.split()[0]
    replace_word = words_dict.get(word)
    lines[index] = line.replace(word, replace_word)

print(f"Результирующий список: {lines}")
write_lines_to_file(lines)
