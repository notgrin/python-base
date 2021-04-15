"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
 «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
  Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
   @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.day, self.moth, self.year = self.extract_parts(date)
        self.validate(self.day, self.moth, self.year)

    def __str__(self):
        return f'{self.day:02}.{self.moth:02}.{self.year:04}'

    @classmethod
    def extract_parts(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if not (1 <= month <= 12):
            raise ValueError('Месяц в пределах 1-12')

        if month == 2 and year % 4 == 0 and not (1 <= day <= 29):
            raise ValueError(f'В феврале {year} года - 29 дней')
        if month == 2 and year % 4 != 0 and not (1 <= day <= 28):
            raise ValueError(f'В феврале {year} года - 28 дней')
        # a = [1, 3, 5, 7, 8, 10, 12]
        b = [4, 6, 9, 11]
        if month in b and not (1 <= day <= 30):
            raise ValueError('В этом месяце 30 дней')
        if not (1 <= day <= 30):
            raise ValueError('В месяце не может быть больше 31 дня')


dates = ['36-2-2020',
         '29-2-2021',
         '10-4-2026',
         '31-4-2018',
         '30-12-2021',
         '30-16-2021',
         '62-12-2021',
         ]

for date in dates:
    try:
        dt = Date(date)
        print(dt)
    except ValueError as e:
        print(f'Неверный формат - {e}: [{date}]')
