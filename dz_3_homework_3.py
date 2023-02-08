# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    """
    Функция принимает 3 числа и складывает из них 2 самых больших

    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: sum(list_number) - min(list_number)
    """
    list_number = [num_1, num_2, num_3]
    return sum(list_number) - min(list_number)


print(my_func(100, 200, 99))
