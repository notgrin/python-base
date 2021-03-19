# работа с файлами
# f = open('file.txt', 'w', encoding='utf8')
# for i in range(10):
#     print(f'Hello, I am Steve #{i}', file=f)
# f.close()

# f = open('file.txt', 'r', encoding='utf8')
# # # content = f.read()
# # # print(type(content), content)
#
# for line in f:
#     # print(line, end='')
#     line = line.strip()
#     print(line)
#
#
# # line = f.readline()
# # line = line.strip()
# # print(line)
# f.close()

# ------------------- JSON
import json
# d = {
#     'values': [1, 2, 3, 4, 5],
#     'keys': ['a', 'b', 'c']
# }
# ------------------- JSON - JavaScript Object Notation
# c = json.dumps(d)   # преобразует структуру в строку
# print(type(c), c.encode(encoding='utf8'))
# c = c.replace('values', 'results')
# print(c)
#
# d2 = json.loads(c)  # восстанавливает словарь (рестуктурирует)
# print(d2)
# for k, v in d2.items():
#     print(k, v)
# ------------------- JSON
# with open('serialized_dict.json', 'w', encoding='utf8') as f:
#     json.dump(d, f) # объект записываем в файл
#
# with open('serialized_dict.json', 'r', encoding='utf8') as f2:
#     d2 = json.load(f2)
#
# print(d2)
# print(d)
# ------------------- pickle
import pickle
d = {
    'values': [1, 2, 3, 4, 5],
    'keys': ['a', 'b', 'c']
}
with open('pick', 'wb') as f:
    pickle.dump(d, f)   # передаю объкт и файл, в который нужно сохранить

with open('pick', 'rb') as f2:
    print(f2.read())

with open('pick', 'rb') as f2:
    num2 = pickle.load(f2)

print(num2)
