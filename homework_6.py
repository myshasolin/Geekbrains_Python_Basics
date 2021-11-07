# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products = [
    (1, {'название': 'стол'},
     {'цена': '10000'},
     {'количество': '2'},
     {'ед.измерения': 'шт.'}),
    (2, {'название': 'стул'},
     {'цена': '5000'},
     {'количество': '4'},
     {'ед.измерения': 'шт.'}),
    (3, {'название': 'совесть'},
     {'цена': '999999'},
     {'количество': '1'},
     {'ед.измерения': 'неизвестна'})]

print('_____' * 20)

# вариант решения словарём
print('вариант решения словарём')
print()
number = 1
result = {}
while number != 5:
    name = set()
    list_products = []
    for i in products:
        for x, y in i[number].items():
            list_products.append(y)
            name.add(x)
    name = list(name)
    list_products = list(set(list_products))        # дубль убирает, но и результаты перемешивает
    number += 1
    result[f'{name}'] = list_products
for v, w in result.items():                # так вывод "посимпатичнее"
    print(f'{v}:{w}')

print('_____' * 20)

# вариант решения списком
print('вариант решения списком')
print()
number = 1
while number != 5:
    list_products = []
    name = []
    for i in products:
        for x, y in i[number].items():
            list_products.append(y)
            name.append(x)
    list_products = set(list_products)          # чтоб убрать лишний дубль
    print(f'{set(name)}: {list(list_products)}')
    number += 1

print('_____' * 20)

# вариант решения множеством
print('вариант решения множеством')
print()
number = 1
while number != 5:
    list_products = set()
    name = set()
    for i in products:
        for x, y in i[number].items():
            list_products.add(y)
            name.add(x)
    print(f'{list(name)}: {list(list_products)}')
    number += 1
