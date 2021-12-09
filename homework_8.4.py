# 1) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 2) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#  Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#  изученных на уроках по ООП.

from time import time, ctime


class MyException(Exception):
    def __init__(self, message):
        self.message = message


class OfficeEquipmentWarehouse:  # склад оргтехники
    off_str = ''
    rejection = False

    def __init__(self, office_equipment_dict):  # параметр - список оргтехники
        self._office_equipment_dict = office_equipment_dict

    def __str__(self):  # делаем красивый вывод
        self.in_stock = {}
        for i in self._office_equipment_dict:
            i = str(i)
            self.technic = i[0:-8]
            self.quantity = int(i[-5])
            self.in_stock[self.technic] = self.quantity
        return f'список техники на складе: {self.in_stock}'

    def issue_equipment(self, what, how_many):  # выдать технику. Если на складе меньше запрашиваемого, отказать
        if what.quantity >= how_many:
            what.quantity -= how_many
            self._office_equipment_dict.remove(what)
            self._office_equipment_dict.append(what)
            OfficeEquipmentWarehouse.off_str = str(what)[:-8]
            return f'{OfficeEquipmentWarehouse.off_str}'
        else:
            OfficeEquipmentWarehouse.rejection = True

    def accept_the_technique(self, what, how_many):  # забрать технику обратно на склад
        what.quantity += how_many
        self._office_equipment_dict.append(what)
        OfficeEquipmentWarehouse.off_str = str(what)[:-8]
        print(f'товар заявлен на возврат: {OfficeEquipmentWarehouse.off_str} {how_many} шт.')

    def recalculate_equipment(self, what, how_many):  # пересчёт на складе после неверных данных на возврат от отдела
        what.quantity -= how_many
        self._office_equipment_dict.remove(what)
        self._office_equipment_dict.append(what)


class OfficeEquipment:  # родитель для оргтехники
    def __init__(self, brand, condition, quantity):  # общие параметры для техники - бренд, состояние, количество
        self.brand, self.condition, self.quantity = brand, condition, quantity

    @staticmethod
    def filling_in_an_object():
        global color_paint, scanning_speed, copy_speed
        filling_in_an_object_list = []
        new_object = None
        the_final_success_message = f'информация о новом товаре записана в файл "recording_about_the_technique"'
        print('создаём новый экземпляр техники!')
        try:
            choice_of_equipment = None
            while not choice_of_equipment:
                choice_of_equipment = input('пиши, что создаём: Printer, Scanner или Xerox: ')
                if choice_of_equipment == 'Printer':
                    break
                elif choice_of_equipment == 'Scanner':
                    break
                elif choice_of_equipment == 'Xerox':
                    break
                else:
                    choice_of_equipment = None
                    print('надо писать только Printer, Xerox или Scanner, другой техникой мы не занимаемся!')
            print(f'итак, создаём {choice_of_equipment}')
            while not new_object:
                try:
                    brand = input('пиши название бренда: ')
                    condition = input('в каком состоянии? ')
                    quantity = 0
                    while not 0 < quantity < 10:
                        quantity = int(input('какое кол-во? Товар за 1 раз принимается до 10-ти шт! '))
                    if choice_of_equipment == 'Printer':
                        question = input('цветной или как? Пиши "да" или "нет": ')
                        if question == 'нет':
                            color_paint = False
                        elif question == 'да':
                            color_paint = True
                        else:
                            raise MyException('надо писать "да" или "нет" и ничего другого, такие правила\nначнём '
                                              'заново')
                    elif choice_of_equipment == 'Scanner':
                        scanning_speed = int(input('пиши цифру - количество сканирования листов в минуту: '))
                    elif choice_of_equipment == 'Xerox':
                        copy_speed = int(input('пиши цифру - количество копирования листов в минуту: '))
                except MyException as text:
                    print(text)
                except ValueError:
                    print('что-то в цифрах указано неверно\nначнём заново')
                else:
                    if choice_of_equipment == 'Printer':
                        new_object = Printer(brand, condition, quantity, color_paint)
                        print('\nуспешно создан товар:', new_object)
                        text = f'товар: Printer ({brand}, {condition}, {quantity}, {color_paint})'
                        OfficeEquipment.RecordingAboutTheTechnique(text)
                        print(the_final_success_message)
                    elif choice_of_equipment == 'Scanner':
                        new_object = Scanner(brand, condition, quantity, scanning_speed)
                        print('\nуспешно создан товар:', new_object)
                        text = f'товар: Scanner ({brand}, {condition}, {quantity}, {scanning_speed})'
                        OfficeEquipment.RecordingAboutTheTechnique(text)
                        print(the_final_success_message)
                    elif choice_of_equipment == 'Xerox':
                        new_object = Xerox(brand, condition, quantity, copy_speed)
                        print('\nуспешно создан товар:', new_object)
                        text = f'товар: Xerox({brand}, {condition}, {quantity}, {copy_speed})'
                        OfficeEquipment.RecordingAboutTheTechnique(text)
                        print(the_final_success_message)
                    filling_in_an_object_list.append(new_object)
                    print(f'объект в памяти: {filling_in_an_object_list}')
        except UnboundLocalError:
            print('надо писать только Printer, Xerox или Scanner, другой техникой мы не занимаемся!')

    @staticmethod
    def RecordingAboutTheTechnique(text):
        with open('recording_about_the_technique.txt', 'a', encoding='utf-8') as f:
            record = f'{ctime(time())}\nсоздана новая запись о товаре\n{text}\n\n'
            f.writelines(record)


class Printer(OfficeEquipment):
    def __init__(self, brand, condition, quantity, color_paint=True):
        super().__init__(brand, condition, quantity)
        self.color_paint = color_paint  # свой параметр = цветная краска

    def __str__(self):
        return f'принтер {self.brand} - {self.quantity} шт.'


class Scanner(OfficeEquipment):
    def __init__(self, brand, condition, quantity, scanning_speed):
        super().__init__(brand, condition, quantity)
        self.scanning_speed = scanning_speed  # свой параметр - скорость сканирования

    def __str__(self):
        return f'сканер {self.brand} - {self.quantity} шт.'


class Xerox(OfficeEquipment):
    def __init__(self, brand, condition, quantity, copy_speed):
        super().__init__(brand, condition, quantity)
        self.copy_speed = copy_speed  # ской параметр - скорость копирования

    def __str__(self):
        return f'ксерокс {self.brand} - {self.quantity} шт.'


class Division:  # подразделение

    def __init__(self, title, refers_to_the_warehouse):  # атрибут - название и к какому складу привязаны
        self.title, self.technic, self.refers_to_the_warehouse = title, {}, refers_to_the_warehouse

    def take_the_equipment(self, equipment, how_many):  # взять себе технику - какую и сколько
        self._equipment, self.how_many = equipment, how_many
        self.result = self.refers_to_the_warehouse.issue_equipment(self._equipment, self.how_many)
        if OfficeEquipmentWarehouse.rejection:  # отказ, если запрошено слишком много
            OfficeEquipmentWarehouse.rejection = False
            return 'ОТКАЗАНО!\nнет такого количества на складе!'
        else:
            if self.result not in self.technic:  # наполняем словарь техникой
                self.technic[self.result] = self.how_many
            else:
                self.technic[self.result] += self.how_many
            return f'товар передан отделу: {str(self.technic)[2:-5]} {self.how_many} шт.'

    def return_the_equipment(self, equipment, how_many):  # возвращаем на склад
        self._equipment, self.how_many = equipment, how_many
        try:
            self.refers_to_the_warehouse.accept_the_technique(self._equipment, self.how_many)
            self.result = OfficeEquipmentWarehouse.off_str
            self.technic[self.result] -= self.how_many
            if self.technic[self.result] == 0:  # удаляем инфу о товаре, если его больше нет в отделе
                del self.technic[self.result]
            elif self.technic[self.result] < 0:  # если попытаться сдать больше, чем есть, то
                print('Отмена заявки! Пересчёт, т.к. такого количества товара на возврат в отделе нет!')
                self.technic[self.result] += self.how_many
                self.refers_to_the_warehouse.recalculate_equipment(self._equipment, self.how_many)
            return f'список товаров в отделе: {self.technic}'
        except KeyError:
            self.refers_to_the_warehouse.recalculate_equipment(self._equipment, self.how_many)
            return 'Отмена заявки, т.к. такого товара нет в отделе'


print('заводим технику каждую в свои классы-наследники')
office_equipment_1 = Printer('Epson', 'Good', 2, True)
office_equipment_2 = Scanner('HP', 'New', 9, 100)
office_equipment_3 = Xerox('Canon', 'Average', 3, 50)
office_equipment_4 = Scanner('Avision', 'New', 1, 200)
warehouse_list = [office_equipment_1, office_equipment_2, office_equipment_3, office_equipment_4]
print('формируем экземпляр класса-склад, назовём его warehouse')
warehouse = OfficeEquipmentWarehouse(warehouse_list)
print('выводим на экран словарь с техникой, принятой на склад:')
print(warehouse)
print('формируем экземпляр класса - отдел продаж - sales')
sales = Division('отдел продаж', warehouse)
print('проверим, есть ли что из техники у отдела продаж и получим пустой словарь, т.к. пока ничего нет:')
print(sales.technic)
print('-----' * 100)
print('возьмём отделу продаж со склада технику - 2 сканера HP ')
print(sales.take_the_equipment(office_equipment_2, 2))
print('проверим, появилась ли в отделе продаж техника, о чудо, сканеры переместились в отдел:')
print(sales.technic)
print('проверим, исчезла ли она со склада. Да, так, сканеров стало на 2 меньше:')
print(warehouse)
print('-----' * 100)
print('а теперь вернём сканер на склад:')
print(sales.return_the_equipment(office_equipment_2, 1))
print('проверим, что осталось в отделе:')
print(sales.technic)
print('и проверим, что теперь есть на складе:')
print(warehouse)
print('-----' * 100)
print('выдадим другую технику и проверим склад и наш отдел продаж:')
print(sales.take_the_equipment(office_equipment_1, 1))
print(warehouse)
print(sales.technic)
print('-----' * 100)
print('вернём принтер и посмотрим на отдел продаж и на складе')
print(sales.return_the_equipment(office_equipment_1, 1))
print(warehouse)
print('ну и вернём сканер, после чего в отделе ничего не останется:')
print(sales.return_the_equipment(office_equipment_2, 1))
print('а вот что есть на складе:')
print(warehouse)
print('-----' * 100)
print('попробуем попросить в отдел больше, чем есть на складе. Получим отказ. Товары останутся на своих местах')
print(sales.take_the_equipment(office_equipment_3, 4))
print(warehouse)
print(sales.technic)
print('-----' * 100)
print('передадим отделу поочерёдно два одинаковых принтера и проверим состояние отдела и склада. Всё перемещается:')
print(sales.take_the_equipment(office_equipment_1, 1))
print(sales.technic)
print(warehouse)
print(sales.take_the_equipment(office_equipment_1, 1))
print(sales.technic)
print(warehouse)
print('-----' * 100)
print('Попробуем вернуть то, что есть в отделе, но в бОльшем количестве. Заявка на возврат отменится, '
      'а товар останется в отделе')
print(sales.return_the_equipment(office_equipment_1, 4))
print(sales.technic)
print(warehouse)
print('-----' * 100)
print('Теперь вернём то, чего нет. Заявка так же отменится:')
print(sales.return_the_equipment(office_equipment_4, 1))
print(warehouse)
print(sales.technic)
print('-----' * 100)
print('ну и под финал - попробуем допустить ошибку при создании нового товара. Создадин экземпляр класса Printer в '
      '@staticmethod \nУкажем вместо количества строку и получим ошибку. Аналогично будет с цветом. \nЭкземпляр не '
      'создастся, пока данные не будут введены верно. Данные о создании товара запишутся в файл')
print()
OfficeEquipment.filling_in_an_object()
