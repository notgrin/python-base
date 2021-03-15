"""
Задание 3. Генератор объединения двух списков
Есть два списка:

```
# tutors = [...]
# klasses = [...]

```
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
...
Количество генерируемых кортежей должно быть равно длине списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors,
необходимо вывести последние кортежи в виде: (<tutor>, None), например:
```('Станислав', None)```
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen1():
    if len(tutors) > len(klasses):
        klasses.append(None)
    else:
        tutors.append(None)
    for key, value in zip(tutors, klasses):
        yield key, value


rand1 = gen1()
print(next(rand1))
print(next(rand1))
print(next(rand1))
print(next(rand1))
print(next(rand1))
print(next(rand1))
print(next(rand1))
print(next(rand1))

print(type(rand1)) # доказательство