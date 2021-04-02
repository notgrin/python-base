class Car:
    # color = 'black'
    # doors = 4
    # name = None
    engine = '6 cylinder'

    def __init__(self, name, color='black', doors=4):
        self._name = name
        self.color = color
        self.doors = doors

    def __str__(self):
        return self.describe()

                # ссылка на объект, с которого сейчас работаем
    def describe(self):     # возвращает что-то # в данном случае описание машины
        return f'Car {self.color} {self._name} - {self.doors} дверей, {self.engine}'

class Truck(Car):

    def __init__(self, name, color='black', doors=4, load_limit=1000):
        super().__init__(name, color, doors)  # вызов конструктора базового класса
        # self._name = name
        # self.color = color
        # self.doors = doors
        self.load_limit = load_limit
        self.load = 0

    def __str__(self):
        return f'Truck {self.color} {self._name} - {self.doors} дверей, {self.engine}, load: {self.load} из {self.load_limit}'

    def take_load(self, weight):
        if weight < self.load_limit:
            self.load = weight
        else:
            raise ValueError('нагрузка слишком велика')


car = Truck('Volvo', 'red', 5)

# lst = [1, 2, 3]
# lst.sort()  # вызов метода. атрибут через точку
# print(type(car), car)
# print(car.color)
# print(car.doors)

car.color = 'red'
car.doors = 5
car.name = 'Volvo'
# print(car.color, car.doors, car.name)
# print(car.describe())

car2 = Car('BMW', 'black', 2)    #__str__(self)
# print(car2.color, car2.doors, car2.name)
# print(car2.describe())
# print(Car.describe(car))          # некоторая магия
car3 = Car('Mercedes')
car4 = Car('Mercedes', doors=5)

# print(Car.engine)
#
# print(car)
# print(car2)
# print(car3)
# print(car4)
# car4.engine = '12 cylinder'
#
# Car.engine = '4 cylinder'
#
# print(car)
# print(car2)
# print(car3)
# print(car4)

car.take_load(500)
print(car)
car.take_load(380)
print(car)
car.take_load(1800)
print(car)
