# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка
# можно не запрашивать у пользователя, а указать явно, в программе.

el_list = [12, 2.0, "abcd", "def", True, None]
type_dict = {
    int: "integer",
    float: "float",
    str: "string",
    bool: "boolean"
}

for el in el_list:
    el_type = type_dict.get(type(el))
    if el_type is None:
        print("Type is undefined")
        continue

    print(f"Type is {el_type}")
