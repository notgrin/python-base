# Задание 2
# * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.
# Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

numbers_in_letters = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

print('Программа по переводу слов от 0 до 10 (с английского на русский)')
inserted_english_word = input('Введите число от 0 до 10: ')


def num_translate_adv(english_word):
    if english_word != english_word.lower():
        separated_letter = [element.lower() for element in english_word]
        word_key = numbers_in_letters.get(''.join(separated_letter))
        print(word_key.capitalize())
    else:
        print(numbers_in_letters.get(english_word))


num_translate_adv(inserted_english_word)

