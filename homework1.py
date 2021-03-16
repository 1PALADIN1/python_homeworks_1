
def print_task_separator(task_name):
    print("=================", task_name, "=================")


# 1. Поработайте с переменными, создайте несколько,выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

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
