# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# Вариант решения списком:
print('1) вариант решения списком')
seasons = ['зима', 'весна', 'лето', 'осень']
while True:
    answer = int(input('пиши цифру: '))
    if answer == 1 or answer == 2 or answer == 12:
        print('это у нас:', seasons[0])
        break
    elif answer == 3 or answer == 4 or answer == 5:
        print('это у нас:', seasons[1])
        break
    elif answer == 6 or answer == 7 or answer == 8:
        print('это у нас:', seasons[2])
        break
    elif answer == 9 or answer == 10 or answer == 11:
        print('это у нас:', seasons[3])
        break
    else:
        print('ты написал левую шляпу, давай попробуем ещё раз')
print()

# первый вариант решения словарём при помощи тернарного оператора
print('2) первый вариант решения словарём при помощи тернарного оператора')
season = {
    1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
    7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

answer = int(input('пиши месяц: '))
print(f'это у нас {season[answer]}') if not answer <= 0 and answer <= 12 else \
    print('ты написал левую шляпу, давай попробуем ещё раз')
print()

# Вариант решения словарём с проверкой:
print('3) второй вариант решения словарём с проверкой')
season = {
    1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
    7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

while True:
    answer = int(input('пиши месяц: '))
    if not answer <= 0 and answer <= 12:
        print(f'это у нас {season[answer]}')
        break
    print(answer)
    print('ты написал левую шляпу, давай попробуем ещё раз')
print()

# Ещё ариант решения словарём с проверкой:
print('4) третий вариант решения словарём')
season = {
    'winter': 'зима', 'spring': 'весна', 'summer': 'лето', 'autumn': 'осень'
}
while True:
    answer = int(input('пиши цифру: '))
    if answer == 1 or answer == 2 or answer == 12:
        print('это у нас:', season['winter'])
        break
    elif answer == 3 or answer == 4 or answer == 5:
        print('это у нас:', season['spring'])
        break
    elif answer == 6 or answer == 7 or answer == 8:
        print('это у нас:', season['summer'])
        break
    elif answer == 9 or answer == 10 or answer == 11:
        print('это у нас:', season['autumn'])
        break
    else:
        print('ты написал левую шляпу, давай ещё раз')
print()

# И последнее - короткий красивый вариант словарём, но он без проверки
print('5) четвёртый вариант решения словарём (без проверки)')
season = {
    1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
    7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

answer = season[int(input('пиши месяц: '))]
print(f'это у нас {answer}')
