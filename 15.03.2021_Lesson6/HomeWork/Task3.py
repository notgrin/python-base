"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта,
 а в другом — данные об их хобби. Известно, что при хранении
  данных используется принцип: одна строка — один пользователь,
   разделитель между значениями — запятая. Написать код,
    загружающий данные из обоих файлов и формирующий из них словарь:
     ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
      Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
       меньше записей, чем в файле с ФИО, задаём в словаре значение None.
        Если наоборот — выходим из скрипта с кодом «1».
         При решении задачи считать, что объём данных в файлах во много раз
          меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""
with open('users.csv', 'w', encoding='utf8') as u:
    print('Иванов,Иван,Иванович\nПетров,Петр,Петрович\nМаксимов,Илья,Владимирович\nЩепкин,Костя,Андреев', file=u)
with open('hobby.csv', 'w', encoding='utf8') as h:
    print('скалолазание, охота\nгорные лыжи\nрыбалка\nрыбалка\nрыбалка\nрыбалка\nрыбалка\nрыбалка', file=h)


data_base = {}
with open('users.csv', 'r', encoding='utf8') as users:
    for user in users:
        user = user.strip()
        user = user.replace(',', ' ')
        data_base.setdefault(user)

hobby_list = []
count = 0
with open('hobby.csv', 'r', encoding='utf8') as hobbies:
    for hobby in hobbies:
        hobby = hobby.strip()
        hobby_list.append(hobby)

if len(hobby_list) < len(data_base.keys()):
    hobby_list.append(None)
else:
    exit(1)

while count < len(data_base.keys()):
    for i in data_base.keys():
        data_base[i] = hobby_list[count]
        count += 1

print(data_base)