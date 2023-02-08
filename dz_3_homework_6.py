# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

"""
Первая функция реализована через lambda. Она принимает одно слово и выводит его с прописной первой буквой

    :param: word (мама)
    :return: Word (Мама)
"""

int_func_upper = (lambda word: word.capitalize())


def text_func_upper(input_text):
    """
    Функция принимает строчку из слов и возвращает ту же строчку, но с прописной первой буквой в каждом слове

        :param input_text: a set of words (мама мыла раму)
        :return: A Set Of Words (Мама Мыла Раму)
    """
    input_text = input_text.split(' ')
    list_text = []
    for i in input_text:
        i = i.capitalize()
        list_text.append(i)
    new_text = ' '.join(list_text)
    return new_text


print(int_func_upper(input('пиши слово: ')))

print(text_func_upper(input('пиши несколько слов: ')))
