# Задание 3
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

source_list_index = 0
while source_list_index < len(source_list):
    element = source_list[source_list_index]
    if element.isdigit():
        source_list[source_list_index] = f'{int(element):02d}'
        source_list.insert(source_list_index, '"')
        source_list.insert(source_list_index + 2, '"')
        source_list_index += 3
    elif (element[0] == '+' or element[0] == '-') and element[1:].isdigit():
        sign = element[0]
        source_list[source_list_index] = sign + f'{int(element[1:]):02d}'
        source_list.insert(source_list_index, '"')
        source_list.insert(source_list_index + 2, '"')
        source_list_index += 3
    else:
        source_list_index += 1

# print(target_list)
result = ' '.join(source_list)
print(result)