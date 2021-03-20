# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# решение через dict
def dict_solution(month):
    months = {
        12: "зима",
        1: "зима",
        2: "зима",
        3: "весна",
        4: "весна",
        5: "весна",
        6: "лето",
        7: "лето",
        8: "лето",
        9: "осень",
        10: "осень",
        11: "осень"
    }

    season = months.get(month)
    if season is None:
        print("Время года не определено!")
        return

    print(f"Время года: {season}")


# решение через list
def list_solution(month):
    if month > 12 or month < 1:
        print("Время года не определено!")
        return

    seasons = ["зима", "весна", "лето", "осень"]
    month %= 12
    season_length = 3

    season_index = month // season_length
    season = seasons[season_index]
    print(f"Время года: {season}")


input_month = int(input("Номер месяца: "))

dict_solution(input_month)
list_solution(input_month)
