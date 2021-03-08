# Задание 4
# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?

print('Когда введете все имена введите 0 (ноль) и появится словарь')
print('Вводите имена в любой последовательности')


def thesaurus_adv():
    count = 1
    insert = None
    names = []
    while insert != '0':
        insert = input(f'Введите имя {count}: ')
        count += 1
        names.append(insert.title())
    names.pop()
    print(names)

    surname_dict = {}
    name_dict = {}
    for name in names:
        first_name, surname = name.split()
        surname_dict.setdefault(surname[0], name_dict)
        name_dict.setdefault(first_name[0], [])
        name_dict[first_name[0]].append(name)

    # print(name_dict)
    import pprint
    pprint.pprint(surname_dict)


thesaurus_adv()

