# Задание 3
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

# def thesaurus():
#     pass

import pprint

user = {'И': ['Ирина', 'Сказка', 'Кошелек']}

# insert = input('Введите имя, которое нужно добавить в словарь: ')
# user.setdefault(insert[0], insert)
# insert = None
#

#     first_name = {insert[0], insert}
#     # print(first_name)
#     user.update(first_name)
#     # print(user)


# user.popitem()
# print(user)

print('Когда введете все имена введите 0 (ноль) и появится словарь')
print('Вводите имена в любой последовательности')
count = 1
insert = None
names = []

while insert != '0':
    insert = input(f'Введите имя {count}: ')
    count += 1
    names.append(insert.capitalize())

names.pop()
print(names)

name_list = {}

for name in names:
    name_list.setdefault(name[0], [])
    name_list[name[0]].append({name})

import pprint

pprint.pprint(name_list)