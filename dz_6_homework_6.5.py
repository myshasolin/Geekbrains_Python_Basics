# Реализовать класс Stationery (канцелярская принадлежность).Определить в нем атрибут title (название) и метод draw(от-
# рисовка).Метод выводит сообщение “Запуск отрисовки.”Создать три дочерних класса Pen (ручка), Pencil (карандаш),Handle
# (маркер).В каждом из классов реализовать переопределение метода draw.Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    numbers = 0

    def __init__(self, title):
        self.title = title
        Stationery.numbers += 1

    def draw(self):
        return f'\nЗапуск отрисовки № {Stationery.numbers}\nрисуем вот чем - {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки № {Stationery.numbers}\nрисуем при помощи {self.title} всякие пейзажи'


class Pencil(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки № {Stationery.numbers}\n{self.title} да поможет нам'

class Handle(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки № {Stationery.numbers}\nневозможно нарисовать ничего приличного при помощи ' \
               f'{self.title}. Я не умею и вы не беритесь'


# a = Stationery('мел')
# print(a.draw())

b = Pen('ручка')
print(b.draw())
c = Pencil('карандаш')
print(c.draw())
d = Handle('маркер')
print(d.draw())
