# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

name = input('пиши число: ')
name2 = name * 2
name3 = name * 3

result = int(name) + int(name2) + int(name3)

print()
print(f'решение: {result}')
