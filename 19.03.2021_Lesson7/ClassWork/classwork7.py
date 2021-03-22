from utils.helpers import print_current_work_dir
import os

# print(os.path.curdir)
# . - текущий каталог (рабочий каталог)

# print(os.path.abspath(os.path.curdir))
# абсолютный путь

# print_current_work_dir()

# print(os.listdir()) # содержимое текущего каталога

filename = 'classwork7.py'
if os.path.exists(filename): #  and we_have_access(filename)
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read())
        print_current_work_dir()
# except:
#     print('something went wrong')

# EAFP - Easy Ask for Forgiveness than Permission