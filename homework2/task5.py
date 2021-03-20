# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2]

while True:
    input_value = input("Enter rating value (q - exit program): ")
    if input_value == "q":
        break

    rating_value = int(input_value)
    rating.append(rating_value)
    rating.sort(reverse=True)
    print(f"Rating: {rating}")
