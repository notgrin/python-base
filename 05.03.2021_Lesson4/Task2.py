"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""


import requests
import requests.utils as utils

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


get_currency_rate('USD', 'EUR', 'AUD', 'GBP')