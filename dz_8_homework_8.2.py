# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, message):
        self.message = message


def arithmetic_division():
    try:
        x = int(input('пиши делимое: '))
        y = int(input('пиши делитель: '))
        if y == 0:
            raise MyException('кто ж на 0 делит-то, нельзя же, это все знают, даже я')
    except MyException as mess:
        return mess
    except ValueError:
        return 'у тебя там вместо цифры шляпа какая-то указана, проверь'
    else:
        return f'В стиле Мистера Маки:"всё прошло без ошибочек, п’нятненько?"' \
               f'\nполучи результ деления: {round((x / y), 2)}'


print(arithmetic_division())
