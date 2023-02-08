# Реализуйте базовый класс Car.У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    numbers = 0

    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name = speed, color, name
        self.is_police = is_police
        Car.numbers += 1
        print(f'\nтачка нумбер {Car.numbers}. ', end='')

    def go(self):
        if self.speed > 0:
            message = 'полный вперёд!'
        elif self.speed < 0:
            message = 'задний ход, Карл'
        else:
            message = Car.stop(self)
        return message

    def stop(self):
        if self.speed == 0:
            message = 'встала'
        else:
            message = 'куда-то мы таки едем, не стоим.. а вот куда? вызови ".go()" и узнаешь'
        return message

    def turn(self, direction):
        if self.speed != 0:
            if direction == 'право' or direction == 'right':
                message = 'направо повернула'
            elif direction == 'лево' or direction == 'right':
                message = 'повернула налево'
            else:
                message = 'куда она там повернула, науке пока неизвестно, наука пока не в курсе дела'
        else:
            message = f'куда ей поворачивать? Она ж не едет, у неё скорость {self.speed} кэмэ'
        return message

    def show_speed(self):
        return f'текущая скорость: {self.speed} кэмэ'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'это TownCar')

    def show_speed(self):
        if self.speed > 60:
            return f'куда погнал со скоростью в {self.speed} кэмэ?? Выше 60-ти низя'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'это SportCar')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'это WorkCar')

    def show_speed(self):
        if self.speed > 40:
            return f'куда погнал со скоростью в {self.speed} кэмэ?? Выше 40-а низя'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'это PoliceCar')
        self.is_police = True


a = SportCar(60, 'red', 'Audi')
print(a.go())
print(a.show_speed())
print(a.is_police)

b = TownCar(90, 'green', 'Lada Kalina-Malina')
print(b.show_speed())

c = WorkCar(50, 'orange', 'ведро с гайками')
print(c.stop())
print(c.turn('right'))
print(c.show_speed())
print(c.is_police)
print(c.name)

d = PoliceCar(0, 'white', 'Crown Vic')
print(d.turn('право'))
print(d.stop())
print(d.is_police)
