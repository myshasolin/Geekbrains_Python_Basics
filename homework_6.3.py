# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    count = 0

    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'зепеха': wage, 'бонус': bonus}
        Worker.count += 1
        print(f'работник нумбер {Worker.count}')


class Position(Worker):

    def get_full_name(self):
        return f'полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'зепеха: {sum(self._income.values())} денег'


a = Position('Мишаня', 'Солин', 'самый важный и отважный', 100000, 3000)
print(a.get_full_name())
print(a.get_total_income())
print(f'должность - {a.position}')
print()
b = Position('Иван Иваныч', 'Иванов', 'безработный, бедный, но гордый', 12792, 208)
print(b.get_full_name())
print(b.get_total_income())
print(f'должность - {b.position}')
print(f"бонус тут скромный - {b._income['бонус']} денег")
