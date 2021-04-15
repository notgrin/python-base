"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
 Проверьте его работу на данных, вводимых пользователем.
  При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyDivisionByZero(Exception):
    pass


def my_div(a, b):
    if b == 0:
        raise MyDivisionByZero('На 0 делить нельзя')
    return a / b


while True:
    a = int(input('Введите делимое (или -1 для остановки): '))
    if a == -1:
        break
    b = int(input('Введите делитель: '))

    try:
        c = my_div(a, b)
    except MyDivisionByZero as e:
        print('Ошибка', e)
    else:
        print(f'{a} / {b} = {c}')
