# Создать (не программно) текстовый файл со следующим содержимым: One — 1, Two — 2, Three — 3, Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file_dz_5.4_eng.txt', encoding='utf-8') as f1, open('file_dz_5.4_rus.txt', 'w+', encoding='utf-8') as f2:
    print('\nстарый список из файла "file_dz_5.4_eng.txt":\n')
    for i in f1:
        print(i, end='')
        word = i.split(' ')[0]
        if word in my_dict:
            word = my_dict[word]
        result = f"{word} {i.split(' ')[1]} {i.split(' ')[-1]}"
        f2.writelines(result)
    f2.seek(0)
    print('\n\nновый список. Он записался в файл "file_dz_5.4_rus.txt":\n')
    for i2 in f2:
        print(i2, end='')
print()
