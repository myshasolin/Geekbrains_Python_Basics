# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('file_dz_5.7.txt', encoding='utf-8') as f, open('file_dz_5.7.json', 'w', encoding='utf-8') as js:
    my_dict_profit, my_dict_average_profit = {}, {}
    company_number, company_counter, average_profit, sum_profit = 1, 0, 0, 0
    print('список фирм и их прибыль:')
    for i in f:
        name, revenue, costs = i.split()[0], float(i.split()[-2]), float(i.split()[-1])
        profit = revenue - costs
        if profit > 0:
            sum_profit += profit
            company_counter += 1
        print(f'{company_number}) {i.split()[1]} {name}, прибыль: {profit} денег')
        company_number += 1
        my_dict_profit[name] = profit
    average_profit = sum_profit / company_counter
    print(f'\nсредний доход: {average_profit} денег')
    my_dict_average_profit['средний доход'] = average_profit
    print('\nа вот что мы записали в "file_dz_5.7.json":')
    my_dict = [my_dict_profit, my_dict_average_profit]
    print(my_dict)
    str_in_write = json.dumps(my_dict)
    js.write(str_in_write)
