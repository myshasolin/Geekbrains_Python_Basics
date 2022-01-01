# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file_dz_5.5.txt', 'w+', encoding='utf-8') as f:
    numbers = input('пиши числа через пробел: ')
    f.write(f'записаны числа: {numbers}')
    f.seek(0)
    for i in f:
        my_list = i.split(' ')
    list_slice = my_list[2:]
    result = sum([int(i) for i in list_slice])
    f.write(f'\nсумма введённых чисел: {result}')
    print(f'\nсумма чисел: {result} \nсами числа и результат их сложения записаны в файл')
