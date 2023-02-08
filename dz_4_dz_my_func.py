def payroll_calculation(x, y, z):
    """
    Функция возьмёт и посчитает нам зепешку

    :param x: argv[2]
    :param y: argv[3]
    :param z: argv[4]
    :return: argv[2] * argv[3] + argv[4]
    """
    result = (int(x) * int(y)) + int(z)
    return result


def my_func(num):
    """
    Функция вернёт факториал числа, выводя поочерёдно результат с 1! и до n!

    :param num: int
    :return: int*int
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
        yield result


if __name__ == '__main__':
    payroll_calculation(100, 200, 5)
