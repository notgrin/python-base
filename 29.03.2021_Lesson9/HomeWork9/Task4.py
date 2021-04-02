"""
4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка).
 Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список.
 Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}: «Запуск отрисовки»'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'В данный момент используется {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'В данный момент используется {self.title}. Запуск отрисовки карандашем'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'В данный момент используется {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Карандаш')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
