"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
 можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
  Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    def inner_func(*args, **kwargs):
        # print('args:', args, 'kwargs:', kwargs)
        res = func(*args, **kwargs)
        print('result', res)
        return res

    return inner_func


@type_logger
def calc_cube(a):
    return a ** 3


@type_logger
def my_sum(a, b):
    return a + b


a = calc_cube(5)
print(type(a), a)
# my_sum(3, 4)