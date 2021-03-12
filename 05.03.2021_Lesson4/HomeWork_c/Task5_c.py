"""
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""

import sys

from utils import get_currency_rate

currencies = sys.argv[1:]
if len(currencies) > 0:
    for currency in currencies:
        currency_rate, course_date = get_currency_rate(currency)
        print(currency.upper(), currency_rate, course_date)
else:
    print('Передайте набор')