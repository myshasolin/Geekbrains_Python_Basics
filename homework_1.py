# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [20, True, 'святая истина', None, 66.6, (1, 2, 3)]

for i in my_list:
    print(i, f'- тип {type(i)}')