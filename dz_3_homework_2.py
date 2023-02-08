# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def dossier(name='нет данных', surname='нет данных', year='нет данных', city='нет данных',
            email='нет данных', tel='нет данных'):
    """
    функция собирает данные и выводит их одной строкой. При отсутствии параметра пишет "нет данных"
    :param name: list
    :param surname: list
    :param year: list
    :param city: list
    :param email: list
    :param tel: list
    :return: list('name+surname+year+city+email+tel')
    """

    result = (f'имя - {name}, а фамилия - {surname}, год рождения - {year}, город - {city},'
              f' почта - {email}, ну и телефон - {tel}')
    return print(result)


dossier(name='Иван', surname='Иванов', year='1987', city='Подмоскоево',
        email='lyalya@topolya.ru', tel='+7322233322233')
