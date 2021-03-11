"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.
"""

import requests
import requests.utils as utils
import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)


def get_currency_rate(*args):
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    for a in args:
        start = content.find(a)
        end = content[start:].find('</Value>')
        currency = content[start: (start+end)]
        first_part = currency[:3]
        second_part = currency[-4:]
        main_part = currency[-8: -4]
        x = []
        for number in main_part:
            if number.isdigit():
                x.extend(number)
        full_part = ''.join(x)
        print(f'{first_part}: {int(full_part)},{int(second_part)} руб')

    time_start = content.find('ValCurs Date="')
    time_end = content[time_start: (time_start + 24)]
    # print(time_end)
    time_now = []
    for element in time_end:
        if element.isdigit() or element == '.':
            time_now.append(element)

    date = ''.join(time_now)
    year = date[-4:]
    y = int(year)
    month = date[3:5]
    m = int(month)
    day = date[:2]
    d = int(day)

    d1 = datetime.date(y, m, d)
    print(f'Курсы валют действую до: {d1}')


get_currency_rate('USD', 'EUR', 'AUD', 'GBP')
