# ----------------------- 1.сложение двух объектов через + (__add__)
# class Int:
#     def __init__(self, number):
#         self.number = number
#
#     def __str__(self):
#         return str(self.number)
#
#     def __add__(self, other):
#         summary = Int(self)
#         summary.number = self.number + other.number
#         return summary
#
#
# a = Int(3)
# b = Int(4)
#
# # сложение двух объектов через +
# c = a + b
# print(c)

# ----------------------- 2.сложение двух объектов через + (__add__)
# class Parking:
#     def __init__(self):
#         self.list_cars = []
#         self.name = 'No name'
#
#     def __str__(self):
#         return ', '.join(self.list_cars)
#
#     def add(self, car):
#         self.list_cars.append(car)
#
#     def remove(self, car):
#         self.list_cars.remove(car)
#
#     def __add__(self, other):
#         parking = Parking()
#         parking.list_cars = self.list_cars + other.list_cars
#         return parking
#
#     # ----------------------- __getitem__ - если нужно получить i-ый элемент из объекта
#     def __getitem__(self, index):
#         return self.list_cars[index]
#
#     # ----------------------- __len__ - позволяет вернуть длину объекта(в данном случае списка)
#     def __len__(self):
#         return len(self.list_cars)
#
#     # ----------------------- __setattr__ - позволяет перехватить момент,
#     # когда атрибуту присваивается новое значение
#     def __setattr__(self, key, value):
#         # -------- v1 - приводим значение к строке
#         if key == 'name':
#             value = str(value)
#         super().__setattr__(key, value)
#         #     super().__...__ - обращаемся к функции родительского объекта
#         # -------- v2 - проверяем является ли значение строкой
#         #     if type(value) != str:
#         #         print("won't work")
#         #     else:
#         #         super().__setattr__(key, value)
#         # else:
#         #     super().__setattr__(key, value)

# ----------------
# a = Parking()
# a.add('Audi')
# a.add('Mercedes')
# a.add('BMW')
# b = Parking()
# b.add('Toyota')
# b.add('Honda')
#
# print(a, len(a))
# print(b, len(b))
# print('-----')
# c = a + b
# print(a)
# print(b)
# print(c)
# ----------------
# __len__ - длина объекта
# print(len(c))
# __getitem__, дабы обратиться к объекту по индексу
# for i in range(len(c)):
#     print(i, c[i])
# ---# ---------------- __setattr__ - например при присвоение атрибута,
# ---# проверить корректен ли его тип
# a = Parking()
# # a.name = 'say my name'
# # a.name = 3
# a.name = type
# print(a.name)

# -------------------- __del__ - вызывается тогда, когда объект освобождается (передается другое значение)
# class DataBase:
#     def __init__(self):
#         print('init A')
#         self.file = open('database.txt', 'r+', encoding='utf-8')
#
#     def get_size(self):
#         return 'Small DataBase'
#
#     # Если работаем с файлами, в методе del нужно закрывать файлы
#     def __del__(self):
#         self.file.close()
#         print('del A')
#
#
# db = DataBase()
# print(db.get_size())
# процесс освобождения памяти - Garbage Collector
# db = 3
# # как только db присваивается другое значение - Python удаляет объект

# -------------------- __del__ (Garbage Collector)
# class DataBase:
#     def __init__(self):
#         print('init A')
#
#     def __del__(self):
#         print('del A')

# -----
# db = DataBase()
# print('db = DataBase()')
# a = db
# print('a = db')
# db = 3
# print('db = 3')
# a = 'nothing'
# print("a = 'nothing'")
# -----

# db1 = DataBase()
# db2 = DataBase()
#
# db1.xxx = db2
# db2.xxx = db1
#
# db1 = 'no idea'
# db2 = 3

# ----- __call__
# class DataBase:
#     def __init__(self):
#         print('init A')
#
#     def __del__(self):
#         print('del A')
#
#     def __call__(self, *args, **kwargs):
#         print(args, kwargs)
#
#
# db = DataBase()
# db()
# db(1)
# db(1, args=234, kwargs={123: 'Hi', 456: 'Bye'})

# ------------------------- Переопределение методов
# class A:
#     def method(selfs):
#         pass
#
#
# class B(A):                                # Новый класс, что бы не было повторений
#     class C(A):
#         def method(self):
#             A.method(self)
#
#     def m2(self):
#         print('Hello')
#
#
# class C(B):
#     def method(self):
#         super().method()        # вместо этого выражения A.method(self)
#     # def m2(self):                 # super() более универсален
#     #     print('Hello')
#
#
# class D(B):
#     def method(self):
#         super().method()
#     # def m2(self):
#     #     print('Hello')
#
#
# class E(A):
#     def method(self):
#         A.method(self)
#
# -------------------- Интерфейс == набор методов
# class A:
#     def __len__(self):  # __len__ поддерживает интерфейс определения длины
#         return 3            # наличие метода len внутри класса
#
#
# a = A()                 # экземпляр класса
# len(a)

# ------------------
# r = range(10)
# print(type(r))
# for i in r:
#     print(i)
# ------------------ как устроен итератор
#--
# class IterParking:
#     def __init__(self, objects):
#         self.objects = objects
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.objects):
#             obj = self.objects[self.index]
#             self.index += 1
#             return obj
#         raise StopIteration
#--
#
# class Parking:
#     def __init__(self):
#         self.list_cars = []
#         self.name = 'No name'
#         # self._total_space = self.get_total_space()       # get_total_space() - долго работающий метод
#         self._total_space = None
#
#     def __str__(self):
#         return ', '.join(self.list_cars)
#
#     def add(self, car):
#         self.list_cars.append(car)
#
#     def remove(self, car):
#         self.list_cars.remove(car)
#
#     # def __getitem__(self, index):
#     #     return self.list_cars[index]
#     #
#     # def __len__(self):
#     #     return len(self.list_cars)
#
#     def __iter__(self):
#         return IterParking(self.list_cars)
#
#     # def get_occupied_space(self):
#     #     return len(self.list_cars) * 20
#
#     @property                   # то, где оборачиватся @property , не может быть доп параметров
#     def occupied_space(self):
#         return len(self.list_cars) * 20
#
#     @property                   # отложенные вичисления, при их необходимости
#     def total_space(self):
#         if self._total_space is None:
#             self._total_space = self.get_total_space()
#         return self._total_space
#
#     def get_total_space(self):
#         from time import sleep
#         sleep(2)
#         return 300
#
#
# parking = Parking()
# parking.add('Volvo')
# parking.add('BMW')
# parking.add('Lada')
#
# # for car in parking:     # итерация возможна благодаря __getitem__
# #     print(car)
#
# # print(parking.get_occupied_space())
# print(parking.occupied_space)   # упрощается код благодаря @property
# print(parking.total_space)

"""композиция(агрегация) - когда есть несколько классов"""
# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# class B:
#     def __init__(self, a):
#         self.a = a
#
#
# a = A('hello')
# b = B(a)
#
# print(b.a.name)

"""Абстрактный базовый класс"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_size2(self):
        pass


class B(A):         # если не определены все абстрактные методы, мы не сможем их использовать, т.к. B - все ещё абстрактный
    def get_size(self):
        return 3


class C(B):
    def get_size2(self):
        return 5

c = C()
print(c.get_size())