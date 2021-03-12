"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.
"""

import requests
import datetime
import decimal


def get_currency_rate(currency):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if resp.status_code != 200:
        print('сайт не доступен')
        exit()
    content = resp.content.decode('windows-1251')

    day, month, year = list(map(int, content.split('Date="')[1].split('"', maxsplit=1)[0].split('.')))
    course_date = datetime.date(year, month, day)

    parts = content.split('</Valute><Valute')
    currency_code = ('<CharCode>' + currency.upper() + '</CharCode>')
    for part in parts:
        if currency_code in part:
            currency_rate = decimal.Decimal(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
            break
    else:
        currency_rate = None

    return currency_rate, course_date


for currency in ['USD', 'eur', 'CAD']:
    currency_rate, course_date = get_currency_rate(currency)
    print(currency.upper(), currency_rate, course_date)


