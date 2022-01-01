# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('file_dz_5.2.txt', encoding='utf-8') as f:
    print(f'вот что в нашем файле записано:\n\n{f.read()}')
    f.seek(0)
    reeds = f.readlines()

    print(f'\nИтого\nколичество строк: {len(reeds)}')
    str_num = 1
    for i in reeds:
        print(f'в {str_num} строке слов: {len(i.split())} шт.')
        str_num += 1
