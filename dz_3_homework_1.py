# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def numbers(num_1, num_2):
    """
    Делит числа первое на второе

    :param num_1: int
    :param num_2: int
    :return: num_1/num_2
    """
    numbers_division = round((num_1 / num_2), 2)
    return numbers_division


exiting_the_loop = None
while not exiting_the_loop:
    try:
        number_1 = float(input('пиши первое число: '))
        number_2 = float(input('пиши число второе: '))
        result = numbers(number_1, number_2)
        exiting_the_loop = True
    except ZeroDivisionError:
        print('на 0 делить нельзя вообще-то, даваё ещё раз')
    except ValueError:
        print('надо написать число, а не то, что ты там написал.. давай ещё раз')
    else:
        print(f'поделим и получим: {result}')
