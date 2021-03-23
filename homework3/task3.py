# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    numbers = (num1, num2, num3)
    total_sum = sum(numbers)

    result = total_sum - numbers[0]
    for i in range(1, len(numbers)):
        pair_sum = total_sum - numbers[i]
        if result < pair_sum:
            result = pair_sum

    return result


print(f"Max sum: {my_func(23, 89, 45)}")
print(f"Max sum: {my_func(11, -90, 12)}")
print(f"Max sum: {my_func(10000, 200, 1200)}")
