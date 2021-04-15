"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
  общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self):
        self.warehouse = []


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Equipment):
    def __init__(self, name, price, print_size):
        super().__init__(name, price)
        self.print_size = print_size


class Scanner(Equipment):
    def __init__(self, name, price, is_colour):
        super().__init__(name, price)
        self.print_size = is_colour


class Xerox(Equipment):
    def __init__(self, name, price, is_manual):
        super().__init__(name, price)
        self.print_size = is_manual
