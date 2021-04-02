"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os


empty_char = "-"
subject_types = ("(л)", "(пр)", "(лаб)")


def parse_studies(input_hours):
    """
    Возвращает количество занятий из входных данных
    :param input_hours: string
    :return: int
    """
    if input_hours == empty_char:
        return 0

    for s in subject_types:
        input_hours = input_hours.replace(s, "")

    return int(input_hours)


with open(os.path.join("files", "file6.txt"), "r") as f:
    result = {}
    for line in f:
        data = line.split(":")
        studies = data[1].split()
        total_studies = parse_studies(studies[0]) + parse_studies(studies[1]) + parse_studies(studies[2])
        result.update({data[0]: total_studies})

    print(result)
