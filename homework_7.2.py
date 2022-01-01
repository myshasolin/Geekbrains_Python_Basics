# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod, ABC


class Clothes(ABC):
    @abstractmethod
    def param(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def param(self):
        result = self.size / 6.5 + 0.5
        return f'расход ткани на пальто: {round(result, 2)}'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def param(self):
        result = 2 * self.height + 0.3
        return f'расход ткани на костюмчег: {round(result, 2)}'


class Working:
    def __init__(self, clothing_name, figure=0):
        self.clothing_name = clothing_name
        self.figure = figure

    def calculation(self):
        quantity, count = 0, 1
        quantity = int(input('сколько штук считаем? '))
        while quantity != 0:
            self.figure += int(input(f'пиши давай размер {count} одёжки: '))
            count += 1
            quantity -= 1
        return ''

    def working(self, checking_for_errors=None):
        while not checking_for_errors:
            try:
                if self.clothing_name == 'пальто':
                    Working.calculation(self)
                    print(Coat(self.figure).param)
                    checking_for_errors = True
                elif self.clothing_name == 'костюм':
                    Working.calculation(self)
                    print(Suit(self.figure).param)
                    checking_for_errors = True
                else:
                    print('урок правописания.Надо писать "пальто" или "костюм" И НИЧЕГО ДРУГОГО!\nпроверь, чего там '
                          'у тебя')
                    checking_for_errors = True
            except ValueError:
                print('это разве размер? Разве это рост?! Давай ещё раз')


a = Coat(100)
print(a.param)

b = Suit(50)
print(b.param)

print()
Working('пальто').working()
print()
Working('костюм').working()
# Working('слива лиловая спелая садовая').working()
