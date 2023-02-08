# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f'\nсложили: {ComplexNumber.__add__(self.num_1, self.num_2)}\n' \
               f'умножили: {ComplexNumber.__mul__(self.num_1, self.num_2)}'

    def __add__(self, other):
        if (self.num_2 + other.num_2) > 0:
            result = f'{self.num_1 + other.num_1}+{self.num_2 + other.num_2}'
        else:
            result = f'{self.num_1 + other.num_1}{self.num_2 + other.num_2}'
        return f'{result}i'

    def __mul__(self, other):
        if (self.num_1 * other.num_2 + self.num_2 * other.num_1) > 0:
            result = f'{self.num_1 * other.num_1 - self.num_2 * other.num_2}+' \
                     f'{self.num_1 * other.num_2 + self.num_2 * other.num_1}'
        else:
            result = f'{self.num_1 * other.num_1 - self.num_2 * other.num_2}' \
                     f'{self.num_1 * other.num_2 + self.num_2 * other.num_1}'
        return f'{result}i'


a = ComplexNumber(2, 8)
b = ComplexNumber(-2, 1)
c = ComplexNumber(-49, 0)
d = ComplexNumber(0, -8)

result_1 = ComplexNumber(a, b)
print(result_1)

result_2 = ComplexNumber(c, d)
print(result_2)

