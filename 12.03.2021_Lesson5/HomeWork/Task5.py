"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

# v1
for element in src:
    if src.count(element) == 1:
        result.append(element)

print(result)

# v2
result = [element for element in src if src.count(element) == 1]
print(result)

# v3
quantity = {}
for element in src:
    quantity.setdefault(element, 0)
    quantity[element] += 1

result = []
for element in src:
    if quantity[element] == 1:
        result.append(element)

print(result)