# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculate_income(hours_param, rate_param, award_param):
    """
    Считает доход сотрудника
    :param hours_param: Выработка в часах
    :param rate_param: Ставка в час
    :param award_param: Премия
    :return: Возвращает итоговый доход
    """
    return (hours_param * rate_param) + award_param


script_name, work_hours, rate_per_hour, award = argv

income = calculate_income(float(work_hours), float(rate_per_hour), float(award))
print(f"Доход: {income}")
