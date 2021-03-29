# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# ----
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    """
    Делает заглавной первую букву строки
    :param word: string
    :return: string
    """
    return str.capitalize(word)


def capitalize_string(input_string):
    """
    Принимает на вход строку и делает каждое слово строки с заглавной буквы
    :param input_string: string
    :return: string
    """
    result = ""

    string_arr = input_string.split()
    for index, el in enumerate(string_arr):
        if index == len(string_arr) - 1:
            result += int_func(el)
            continue

        result += f"{int_func(el)} "

    return result


test_strings = (
    "this is a test string",
    "do not give up the beginning is always the hardest"
)

for test_string in test_strings:
    print(capitalize_string(test_string))
