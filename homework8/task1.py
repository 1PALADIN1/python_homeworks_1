"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    @property
    def date_string(self):
        return self.__date_string

    def __init__(self, date_string):
        self.__date_string = date_string

    @classmethod
    def get_date_numbers(cls, date_string):
        values = date_string.split("-")
        return int(values[0]), int(values[1]), int(values[2])

    @staticmethod
    def validate_date(day, month, year):
        if day <= 0:
            print("День должен быть положительным числом!")
            return

        if month <= 0:
            print("Месяц должен быть положительным числом!")
            return

        if year < 0:
            print("Год не может быть отрицательным числом")
            return

        if month > 12:
            print("Месяц не может быть больше 12!")
            return

        if day > 31:
            print("Количество дней не может быть больше 31!")
            return

        print(f"[{day}-{month}-{year}]: Валидация прошла успешно!")


# test parse date
date1 = Date("20-05-1994")
date2 = Date("11-04-2021")

date1_nums = Date.get_date_numbers(date1.date_string)
date2_nums = Date.get_date_numbers(date2.date_string)
print(f"Дата {date1.date_string}. Число: {date1_nums[0]}, месяц: {date1_nums[1]}, год: {date1_nums[2]}")
print(f"Дата {date2.date_string}. Число: {date2_nums[0]}, месяц: {date2_nums[1]}, год: {date2_nums[2]}")

# test validation
Date.validate_date(date1_nums[0], date1_nums[1], date1_nums[2])
Date.validate_date(date2_nums[0], date2_nums[1], date2_nums[2])

wrong_date1 = Date("00-01-1994")
wrong_date2 = Date("11-15-2021")
wrong_date3 = Date("45-01-2001")

wrong_date1_nums = Date.get_date_numbers(wrong_date1.date_string)
wrong_date2_nums = Date.get_date_numbers(wrong_date2.date_string)
wrong_date3_nums = Date.get_date_numbers(wrong_date3.date_string)

Date.validate_date(wrong_date1_nums[0], wrong_date1_nums[1], wrong_date1_nums[2])
Date.validate_date(wrong_date2_nums[0], wrong_date2_nums[1], wrong_date2_nums[2])
Date.validate_date(wrong_date3_nums[0], wrong_date3_nums[1], wrong_date3_nums[2])
