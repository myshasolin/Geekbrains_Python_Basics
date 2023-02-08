# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

number = int(input('скок элементов запишем? '))
answer_list = []
x = 1
while number != 0:
    element = input(f'пиши {x} элемент: ')
    answer_list.append(element)
    x += 1
    number -= 1
print('вот твой список:')
print(answer_list)

print('поменяем элементы местами!')

answer_list[:-1:2], answer_list[1::2] = answer_list[1::2], answer_list[:-1:2]

print(answer_list)
