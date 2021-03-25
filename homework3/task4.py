# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def custom_pow1(x, y):
    return x ** y


def custom_pow2(x, y):
    result = 1
    for i in range(0, abs(y)):
        result *= x

    return 1 / result


def validate_values(num_value, power_value):

    if num_value <= 0:
        print("Число должно быть положительным!")
        return False

    if power_value >= 0:
        print("Степень должна быть отрицательной!")
        return False

    return True


number = float(input("Введите число: "))
power = int(input("Введите степень: "))

if validate_values(number, power):
    print(f"Результат: {custom_pow1(number, power)}")
    print(f"Результат: {custom_pow2(number, power)}")
