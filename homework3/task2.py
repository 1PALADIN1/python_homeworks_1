# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(first_name, last_name, birth_year, residence_city, email, phone):
    """
    Принимает на вход информацию о пользователе и выводит её в консоль
    :param first_name: string
    :param last_name: string
    :param birth_year: int
    :param residence_city: string
    :param email: string
    :param phone: string
    :return:
    """
    print(f"================USER INFO================")
    print(f"First name: {first_name}\nLast name: {last_name}\nYear: {birth_year}\n"
          f"City: {residence_city}\nEmail: {email}\nPhone: {phone}")


user_info(first_name="Ruslan", last_name="Malinovskiy", birth_year=1994,
          residence_city="Moscow", email="test@email.net", phone="+7(123)456-78-90")
