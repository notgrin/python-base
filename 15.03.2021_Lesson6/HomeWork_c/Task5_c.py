"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной
 строки, чтобы можно было задать путь к обоим исходным файлам
  и путь к выходному файлу со словарём. Проверить работу скрипта
   для случая, когда все файлы находятся в разных папках.
"""
import sys
if len(sys.argv) != 4:
    print('выходной файл, имена, хобби')
    exit(1)

with open(sys.argv[1], 'r', encoding='utf8') as users_f, \
        open(sys.argv[2], 'r', encoding='utf8') as hobby_f, \
        open(sys.argv[3], 'w', encoding='utf8') as result_f:
    while True:
        user = users_f.readline()
        hobby = hobby_f.readline()
        if user:
            user_name = ' '.join(user.strip().split(','))
            hobbies = hobby.strip().split() if hobby else None
            print(user_name, hobbies, file=result_f)
        elif hobby:
            exit(1)
        else:
            break

