
def print_task_separator(task_name):
    print("=================", task_name, "=================")


# 1. Поработайте с переменными, создайте несколько,выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
def task1():
    print_task_separator("Task1")

    greeting_pattern = "Hi, %s"
    age_pattern = "Age: %d"

    name = input("What's your name? ")
    age = int(input("How old are you? "))

    print(greeting_pattern % name)
    print(age_pattern % age)

    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))

    sum_result = first_number + second_number
    sub_result = first_number - second_number
    mul_result = first_number * second_number
    div_result = first_number / second_number

    print(f"{first_number} + {second_number} = {sum_result:.4f}")
    print(f"{first_number} - {second_number} = {sub_result:.4f}")
    print(f"{first_number} * {second_number} = {mul_result:.4f}")
    print(f"{first_number} / {second_number} = {div_result:.4f}")


task1()


# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
def task2():
    print_task_separator("Task 2")

    total_seconds = int(input("Total seconds: "))

    hours = total_seconds // 3600
    minutes = total_seconds // 60 % 60
    seconds = total_seconds % 60

    print(f"Time is {hours:0>2}:{minutes:0>2}:{seconds:0>2}")


task2()


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
def task3():
    print_task_separator("Task 3")

    number = int(input("Number: "))

    i = 0
    current_num = ""
    result = 0
    while i < number:
        i += 1
        current_num += str(number)
        result += int(current_num)

    print(result)


task3()


# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
def task4():
    print_task_separator("Task4")

    number = int(input("Number: "))

    max_number = 0
    while number != 0:
        check_number = number % 10
        if max_number < check_number:
            max_number = check_number

        number //= 10

    print(f"Max number: {max_number}")


task4()


# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
def task5():
    print_task_separator("Task 5")

    proceeds = float(input("Proceeds: "))
    costs = float(input("Costs: "))
    profit = proceeds - costs

    if profit > 0:
        print("The company makes a profit!")
        print(f"Company profitability: {profit / proceeds}")

        emp_number = int(input("The number of employees: "))
        print(f"Profit per employee: {profit / emp_number}")
    else:
        print("The company incurs losses...")


task5()


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
def task6():
    print_task_separator("Task 6")

    a = float(input("a: "))
    b = float(input("b: "))

    day = 1
    result = a

    while result < b:
        result *= 1.1
        day += 1

    print(day)


task6()
