# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(num_1, num_2):
    """
    вариант решения с циклом while

    :param num_1: int
    :param num_2: int
    :return: num_1 ** num_2
    """
    num_2 = abs(num_2)
    result = 1
    while num_2 != 0:
        result *= num_1
        num_2 -= 1
    return round(result, 2)


print(my_func(4.12, -5))

"""
вариант с возведением в степень при помощи lambda-функции и оператора **

:param num_1: int
:param num_2: int
:return: num_1 ** num_2
"""

my_func_2 = (lambda num_1, num_2: round(num_1 ** abs(num_2), 2))
print(my_func_2(4.12, -5))


def my_func_3(num_1, num_2):
    """
    вариант с возведением в степень обычной функцией при помощи оператора **

    :param num_1: int
    :param num_2: int
    :return: num_1 ** num_2
    """
    return round(num_1 ** abs(num_2), 2)


print(my_func_3(4.12, -5))


def my_func_4(num_1, num_2):
    """вариант как не надо было - со встроенной функцией

    :param num_1: int
    :param num_2: int
    :return: pow(num_1, num_2)
    """
    return round(pow(num_1, abs(num_2)), 2)


print(my_func_4(4.12, -5))
