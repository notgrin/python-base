"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class WarehouseError(Exception):
    pass


class Warehouse:
    WAREHOUSE_MAME = 'warehouse'

    def __init__(self):
        self.warehouse = {}

    def __str__(self):
        result = []
        if self.warehouse:
            for department, equipment in self.warehouse.items():
                result.append(f'{department}: {len(equipment)}')
                for equipment, quantity in equipment.items():
                    result.append(f'    {equipment}: {quantity}')
        else:
            result.append('Warehouse is EMPTY')
        result.append('------------------------------')
        return "\n".join(result)

    def get(self, department, equipment):
        return self.warehouse.get(department, {}).get(equipment, 0)

    def set(self, department, equipment, quantity):
        if quantity > 0:
            self.warehouse.setdefault(department, {})
            self.warehouse[department].setdefault(equipment, 0)
            self.warehouse[department][equipment] = quantity
        elif quantity == 0:
            if department in self.warehouse:
                if equipment in self.warehouse[department]:
                    del self.warehouse[department][equipment]

        else:
            raise WarehouseError('Amount of equipment should be more than 0(zero)')

    def change(self, department, equipment, quantity):
        current_quantity = self.get(department, equipment)
        self.set(department, equipment, current_quantity + quantity)

    def add(self, equipment, quantity):
        self.change(self.WAREHOUSE_MAME, equipment, quantity)

    def move_to_department(self, department, equipment, quantity):
        self.change(self.WAREHOUSE_MAME, equipment, -quantity)
        self.change(department, equipment, quantity)

    def return_to_warehouse(self, department, equipment, quantity):
        self.change(department, equipment, -quantity)
        self.change(self.WAREHOUSE_MAME, equipment, quantity)


class Equipment:
    def __init__(self, model_name, price):
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f'{self.__class__.__name__} {self.model_name}'

    def __repr__(self):
        return self.model_name


class Printer(Equipment):
    def __init__(self, model_name, price, print_size):
        super().__init__(model_name, price)
        self.print_size = print_size


class Scanner(Equipment):
    def __init__(self, model_name, price, is_colour):
        super().__init__(model_name, price)
        self.print_size = is_colour


class Xerox(Equipment):
    def __init__(self, model_name, price, is_manual):
        super().__init__(model_name, price)
        self.print_size = is_manual


warehouse = Warehouse()
xerox = Xerox('Xerox 3320', 2000, True)
printer = Printer('HP F-5000', 560, 'A4')

print(warehouse)

warehouse.add(xerox, 5)
warehouse.add(printer, 15)
print(warehouse)

warehouse.move_to_department('Sales', xerox, 3)
warehouse.move_to_department('Sales', printer, 7)
print(warehouse)

warehouse.move_to_department('Bookkeeper', xerox, 1)
warehouse.move_to_department('Bookkeeper', printer, 3)
print(warehouse)

try:
    warehouse.return_to_warehouse('Sales', xerox, 10)
    print(warehouse)
except:
    print('\nNope CAN NOT pick 10\n')

warehouse.return_to_warehouse('Sales', xerox, 1)
print(warehouse)