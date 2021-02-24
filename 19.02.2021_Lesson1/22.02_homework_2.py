# ЗАДАНИЕ 2
#
# Сумма цифр числа
# Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
# Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".


numbers = [-1]
zero = 0


def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


print('Введите "0" если хотите завершить сессию')

while numbers[zero] != 0:
    user_number = int(input('Введите число: '))
    numbers.append(user_number)
    print('Сумма чисел от числа', user_number, 'равняется :', sum_of_digits(user_number))
    zero += 1
    continue
