# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    counter = 0

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def counters(cls):
        cls.counter += 1
        print(f'\nдата нумбер {cls.counter}')

    @classmethod
    def date_output(cls, date_str):
        date_in_numbers = [int(i) for i in date_str.split('-')]
        cls.counters()
        Date.number_validation(date_in_numbers)
        return f'{date_in_numbers[0]:02} {date_in_numbers[1]:02} {date_in_numbers[2]}'

    @staticmethod
    def number_validation(date_in_numbers):
        if 0 < date_in_numbers[0] < 32 and 0 < date_in_numbers[1] < 13 and 1900 < date_in_numbers[2] < 2101:
            print('с датой всё гуд')
        else:
            print('Эй! В дате ошибки! Проверяй внимательней!')


a = Date.date_output('31-12-1901')
print(a)
b = Date.date_output('32-12-1901')
print(b)
