"""
3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
 income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного имени сотрудника get_full_name()
 и дохода с учётом премии get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position,
 вывести на экран имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.
"""


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f'{self.name} {self.surname}'


class Position(Employee):
    def __init__(self, name, surname, _wage, _bonus, position='Baker'):
        super().__init__(name, surname)
        self.position = position
        self.income1 = {'wage': _wage, 'bonus': _bonus}
        self.income2 = _wage + _bonus

    def get_total_income(self):
        return f'{self.get_full_name()}, доход - {self.income2}'


p = Position('Василий', 'Петрович', 505, 500)
print(p.get_total_income())
