# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников. Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('file_dz_5.3.txt', encoding='utf-8') as f:
    print(f'список сотрудников, что записан в файле:\n\n{f.read()}')
    f.seek(0)
    number_of_employees, total_amount, num = 0, 0, 0
    print('\nзп ниже 20000 р. у:')
    for i in f:
        salary, name = float(i.split()[-1]), i.split()[0]
        if salary < 20000:
            num += 1
            print(f'{num}) {name}: {salary} руб.')
        number_of_employees += 1
        total_amount += salary
    average_income = total_amount / number_of_employees
    print(f'\nсредняя величина дохода: {round(average_income, 2)} руб.')
