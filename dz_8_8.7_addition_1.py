# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, actual_part, imaginary_part):
        self.actual_part, self.imaginary_part = actual_part, imaginary_part

    def __str__(self):
        return f'\nсложили: {ComplexNumber.__add__(self.actual_part, self.imaginary_part)}\n' \
               f'умножили: {ComplexNumber.__mul__(self.actual_part, self.imaginary_part)}'

    def __add__(self, other):   # сложение
        global add_imaginary_part
        self.add_actual_part = self.actual_part + other.actual_part         # складываем действительную часть
        list_imaginary_part = [self.imaginary_part, other.imaginary_part]   # формируем список из мнимых частей
        slices, letter = 0, ''
        for i in list_imaginary_part:               # бежим по списку мнимых частей
            if len(i) == 1:                         # и если мнимая чать не сожержит действительной (если она просто i)
                designer = f'{i}'                   # то делаем из неё срочку
            else:                                   # если же мнимая часть состоит из действительной и мнимой
                slices += int(i[:-1])               # то отделяем действительную часть мнимого числа
                letter = i[-1]                      # и мнимую часть мнимого числа
                designer = f'{slices}{letter}'      # и делаем из них строчку
            add_imaginary_part = f'{designer}'      # получаем сложение мнимой части
        if slices >= 0:                             # выводим результат сложения
            return f'{self.add_actual_part}+{add_imaginary_part}'
        else:
            return f'{self.add_actual_part}{add_imaginary_part}'

    def __mul__(self, other):   # умножение (произведение)
        list_imaginary_part = [self.imaginary_part, other.imaginary_part]   # формируем список из мнимых частей
        temporary_list, slices = [], 0
        for i in list_imaginary_part:               # бежим по нему
            if len(i) == 1:                         # и если мнимая чать не сожержит действительной (если она просто i)
                temporary_list.append(1)            # действительная часть = 1
            else:
                slices = int(i[:-1])
                temporary_list.append(slices)       # иначе просто собираем цифры, отбрасывая i
        self_imagin_num = temporary_list[0]         # это первая мнимая переменная
        other_imagin_num = temporary_list[1]        # а это вторая
        elem_1 = self.actual_part * other.actual_part
        elem_2 = self_imagin_num * other_imagin_num
        elem_3 = self.actual_part * other_imagin_num
        elem_4 = self_imagin_num * other.actual_part

        if elem_3 + elem_4 >= 0:                    # выводим результат умножения
            return f'{(elem_1 - elem_2)}+{(elem_3 + elem_4)}i'
        else:
            return f'{(elem_1 - elem_2)}{(elem_3 + elem_4)}i'


print('результат сложения')
num_1 = ComplexNumber(1, '2i')
num_2 = ComplexNumber(4, '-5i')
num_3 = ComplexNumber(0, '2i')
num_4 = ComplexNumber(-3, '1i')

result_1 = ComplexNumber(num_1, num_2)
print(result_1)

result_2 = ComplexNumber(num_3, num_4)
print(result_2)
