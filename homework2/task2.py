# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el_list = []

el_num = int(input("Number of elements in list: "))
i = 0
while i < el_num:
    el_list.append(input("Element: "))
    i += 1

print("Was:", el_list)

for index, el in enumerate(el_list):
    if index % 2 == 0:
        continue

    tmp = el_list[index - 1]
    el_list[index - 1] = el_list[index]
    el_list[index] = tmp

print("Result:", el_list)
