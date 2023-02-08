# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт

from time import sleep

print('первый светофор!')
# вариант светофора по заданию - при вызове класса с 'red' переключает светофор в порядке: red-yellow-green
# при указании другого цвета ('yellow' или 'green') запрашивает введение 'red'
# при указании чего-то другого сообщает об ошибке и завершает скрипт


class TrafficLight:
    __switching = ['red', 'yellow', 'green']

    def __init__(self, color):
        self.__color = color

    def running(self, count=None):
        try:
            while not count:
                if self.__color == 'red':
                    count = True
                    for i in TrafficLight.__switching:
                        print(i)
                        if i == 'red':
                            sleep(7)
                        elif i == 'yellow':
                            sleep(2)
                        elif i == 'green':
                            sleep(4)
                elif self.__color == 'green' or self.__color == 'yellow':
                    print('надо начинать с "red"!')
                    self.__color = input('пиши правильный цвет: ')
                else:
                    raise ValueError
        except ValueError:
            return 'апшипка. Скрипт всё'
        return ''


start = TrafficLight('red')
print(start.running())

print('\nвторой светофор!')
# второй вариант светофора - он запрашивает цвет и переключает светофор в зависимости от указанного цвета:
# пишем 'red', получаем порядок red-yellow-green;
# пишем 'yellow', получаем порядок yellow-red-yellow-green;
# пишем 'green', получаем порядок green-yellow-red;
# Запрос ввода цвета зациклен до той поры, пока не будет введено название одного из 3-х цветов, а не что-то другое


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self, choice=None):
        self.__choice = choice
        while not self.__choice:
            try:
                self.__choice = input('пиши цвет: ')
                if self.__choice == 'red':
                    pass
                elif self.__choice == 'yellow':
                    TrafficLight.__color.insert(0, TrafficLight.__color[1])
                elif self.__choice == 'green':
                    TrafficLight.__color.reverse()
                else:
                    raise ValueError
            except ValueError:
                print('надо цвета писать вообще-то, а не всё попало, что в голову пришло')
                self.__choice = None
            else:
                for i in TrafficLight.__color:
                    print(i)
                    if i == 'red':
                        sleep(7)
                    elif i == 'yellow':
                        sleep(2)
                    elif i == 'green':
                        sleep(4)
        return ''


a = TrafficLight()
print(a.running())
