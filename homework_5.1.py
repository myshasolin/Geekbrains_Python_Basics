# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_str = []

while True:
    text = input('сюда пиши и Enter дави. \nДля завершения дави Enter дважды:\n ')
    my_str.append(text)
    if text == '':
        break
print('файл "file_dz_5.1.txt" создан, текст в него записан')

with open('file_dz_5.1.txt', 'w', encoding='utf-8') as file:
    for i in my_str:
        file.write(i + '\n')
