# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран. Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
with open('file_dz_5.6.txt', encoding='utf-8') as f:
    print(f'\nнаш текст:\n\n{f.read()}')
    f.seek(0)
    for i in f:
        name, information = i.split(':')
        my_list = [y for y in i if y.isdigit() or y == ' ']
        my_list_2 = map(int, ''.join(my_list).split())
        result = sum(my_list_2)
        my_dict[name] = result
print(f'\nА вот и результат! Пришлось таки голову поломать над решением...\n{my_dict}')