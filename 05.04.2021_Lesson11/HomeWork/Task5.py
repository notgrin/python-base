"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на
 склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
  единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class WarehouseError(Exception):
    pass


class Warehouse:
    def __init__(self):
        self.warehouse = {}

    def add(self, equipment, department):
        self.warehouse.setdefault(department, [])
        self.warehouse[department].append(equipment)

    def remove(self, equipment, department):
        try:
            self.warehouse[department].remove(equipment)
        except:
            raise WarehouseError(f'Warehouse - department {department} has no such equipment as {equipment}')

        if department not in self.warehouse:
            raise ValueError('There is no such department')

    def move(self, equipment, department_from, department_to):
        self.remove(equipment, department_from)
        self.add(equipment, department_to)


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


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


warehouse = Warehouse()
xerox = Xerox('Xerox', 2000, True)
warehouse.add(xerox, 'Bookkeeper')
print(warehouse.warehouse)
warehouse.move(xerox, 'Bookkeeper', 'Sales')
print(warehouse.warehouse)