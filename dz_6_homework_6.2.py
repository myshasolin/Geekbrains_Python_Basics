# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см
# толщины полотна. Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    _calculation_of_mass = 0

    def __init__(self, length, width):
        self._length, self._width = length, width

    def result(self, asphalt_mass, thickness):
        Road._calculation_of_mass += 1
        result = round((self._length * self._width * asphalt_mass * thickness) * 0.001)
        return f'\nрасчёт массы № {Road._calculation_of_mass}:\nдлина: {self._length} м.\nширина: {self._width} ' \
               f'м.\nмасса асфальта на 1 кв.метр: {asphalt_mass} кг.\n' \
               f'толщина полотна: {thickness} см.\nИТОГ: {result} т.'


a = Road(length=5000, width=20)
print(a.result(asphalt_mass=25, thickness=5))
b = Road(30, 30)
print(b.result(25, 5))
