# Задание 5
# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов,
# взятых из трёх списков (по одному слову из каждого списка):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random


def get_joke():
    """
    Функция возвращает шутки в виде стоки
    :return: строку
    """
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    return f'{noun} {adverb} {adjective}'


def get_jokes(n):
    """
    Функция возвращает шутки в виде списка строк
    :param n: целое число шуток, которое необходимо вернуть
    :return: список строк
    """
    jokes = []
    for i in range(n):
        jokes.append(get_joke())
    return jokes


print(get_jokes(n=3))


# def get_jokes_unique(n, unique=False):
#     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#     n = min(n, len(nouns), len(adverbs), len(adjectives))
#     jokes = []
#     for i in range(n):
#         noun = random.choice(nouns)
#         adverb = random.choice(adverbs)
#         adjective = random.choice(adjectives)
#         joke = f'{noun} {adverb} {adjective}'
#         jokes.append(joke)
#
#         if unique:
#             nouns.remove(noun)
#             adverbs.remove(adverb)
#             adjectives.remove(adjective)
#     return jokes
#
# print(get_jokes_unique(10))
