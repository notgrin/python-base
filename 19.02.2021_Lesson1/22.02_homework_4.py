# ЗАДАНИЕ 4
#
# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

# module = []
# i = 0
#
# for i in range(100):
#     i += 1
#     module.append(i)

# print(module)
print('Программа для получения нужного окончания')
percent = int(input('Введите проценты от 1 до 100: '))

if percent in range(1, 4):
    print(f'{percent} процента')

if percent in range(5, 21):
    print(f'{percent} процентов')

if percent in range(21, 100, 10):
    print(f'{percent} процент')

if percent in range(22, 100, 10):
    print(f'{percent} процента')

if percent in range(23, 100, 10):
    print(f'{percent} процента')

if percent in range(24, 100, 10):
    print(f'{percent} процента')

if percent in range(25, 100, 10):
    print(f'{percent} процентов')

if percent in range(26, 100, 10):
    print(f'{percent} процентов')

if percent in range(27, 100, 10):
    print(f'{percent} процентов')

if percent in range(28, 100, 10):
    print(f'{percent} процентов')

if percent in range(29, 100, 10):
    print(f'{percent} процентов')

if percent in range(30, 100, 10):
    print(f'{percent} процентов')

