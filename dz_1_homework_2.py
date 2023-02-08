# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

answer_seconds = int(input('пиши секунды: '))

hours = answer_seconds // 3600
minutes = (answer_seconds // 60) % 60
seconds = answer_seconds % 60
print()
print(f'а вот и полное время: {hours:02}:{minutes:02}:{seconds:02}')
