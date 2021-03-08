# Задание 1
# Выяснить тип результата выражений:

# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))

# Задание 2
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку
# до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?
#
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

target_list = []
for element in source_list:
    if element.isdigit():
        target_list.extend(['"', f'{int(element):02d}', '"'])
    elif (element[0] == '+' or element[0] == '-') and element[1:].isdigit():
        sign = element[0]
        target_list.extend(['"', sign + f'{int(element):02d}', '"'])
    else:
        target_list.append(element)

# print(target_list)
result = ' '.join(target_list)
print(result)