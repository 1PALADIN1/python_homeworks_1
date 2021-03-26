# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

analytic_params = ["название", "цена", "количество", "ед"]
analytics = {}
product_struct = []

for param in analytic_params:
    analytics.update({param: []})


def create_struct():
    product_number = 1

    while True:
        command = int(input("================================"
                            "\nУкажите команду:\n1 - Добавить товар\n2 - Собрать аналитику\nКоманда: "))

        if command == 2:
            print(f"Итоговая структура:\n{product_struct}")
            print("================================")
            break

        if command != 1:
            print("Неизвестная команда!")
            product_struct.clear()
            return

        name = input("Введите название: ")
        price = input("Введите цену: ")
        amount = input("Введите количество: ")
        unit = input("Введите единицу измерения: ")

        product_struct.append((product_number, {
            analytic_params[0]: name,
            analytic_params[1]: price,
            analytic_params[2]: amount,
            analytic_params[3]: unit
        }))

        product_number += 1


def collect_analytics():
    for struct_el in product_struct:
        product = struct_el[1]

        for param_name in analytic_params:
            value = product.get(param_name)
            analytics_list = set(analytics.get(param_name))
            analytics_list.add(value)
            analytics.update({param_name: list(analytics_list)})

    print(f"Аналитика:\n{analytics}")


create_struct()
collect_analytics()
