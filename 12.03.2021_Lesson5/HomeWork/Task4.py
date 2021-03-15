"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []
for index_of_previous_element, current_value in enumerate(src[1:]):
    if src[index_of_previous_element] < current_value:
        result.append(current_value)

print(src)
print(result)

# v2
result = [value for index, value in enumerate(src[1:]) if src[index] < value]
print(src)
print(result)