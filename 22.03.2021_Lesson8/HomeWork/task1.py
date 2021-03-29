"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
 имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес
  не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
 имеет ли смысл в данном случае использовать функцию re.compile()?
"""
import re
# email = 'someone@geekbrains.ru'
email = 'someone@geekbrainsru'


def email_parse(email):
    contact = {}
    username_domain = re.compile(r'(\w+)@(\w+[.]\w+)')
    # я не понимаю как работает re.compile и как с этим работать
    username = re.search(r'(\w+)', email)
    a, b = username.span()
    contact['username'] = email[a:b]
    domain = re.search(r'(\w+[.]\w+)', email)
    a, b = domain.span()
    contact['domain'] = email[a:b]
    print(contact)




email_parse(email)

# имеет ли смысл в данном случае использовать функцию re.compile()
# имеет смысл использовать, где большое кол-во данных.