from utils.helpers import print_current_work_dir
import os

# print(os.path.curdir)
# . - текущий каталог (рабочий каталог)

# print(os.path.abspath(os.path.curdir))
# абсолютный путь

# print_current_work_dir()

# print(os.listdir()) # содержимое текущего каталога
# ----------------------------

# filename = 'classwork7.py'
# if os.path.exists(filename): #  and we_have_access(filename)
#     with open(filename, 'r', encoding='utf8') as f:
#         print(f.read())
#         print_current_work_dir()
# except:
#     print('something went wrong')
# ---------------------------------

# EAFP - Easy Ask for Forgiveness than Permission

# ----------------- os.listdir(...)
# folder = r'C:\prog\Python3\Lib\site-packages\aiohttp'
# py_files = [item
#             for item in os.listdir(folder)  # список файлов в папке
#             if item.lower().endswith('.py')]
# print(py_files)

# ----------------- os.path + join()
# folder = r'C:\prog\Python3\Lib\site-packages\aiohttp'
# py_files = [os.path.join(folder, item)
#             for item in os.listdir(folder)
#             if item.lower().endswith('.py')]
# print(py_files)

# ----------------- Django - все папки в корне
# folder = r'C:\prog\Python3\Lib\site-packages\django'
# django_dirs = [item
#                for item in os.listdir(folder)
#                if os.path.isdir(os.path.join(folder, item))]
# print(django_dirs)
# ----------------- создание 1000 папок
import random
# folder = os.path.curdir
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(10 ** 3):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255)
#         for _ in range(random.randrange(10 ** 5)))
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)
# # ----------------- 1.способ - файлы меньше 15кб
# from time import perf_counter
# folder = os.path.curdir
# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files = [item
#                for item in os.listdir(folder)
#                if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
# # ----------------- 2.способ - файлы меньше 15кб
# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files2 = [item.name
#                 for item in os.scandir(folder)
#                 if item.stat().st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
# print(small_files == small_files2)

# # ----------------- 1.способ - 1000 файлов (подсчет)
# from time import perf_counter
#
# folder = os.path.curdir
# start = perf_counter()
# all_files = [item
#              for item in os.listdir(folder)]
# print(len(all_files), perf_counter() - start)
# # ----------------- 2.способ - 1000 файлов (подсчет)
# start = perf_counter()
# all_files2 = [item.name
#               for item in os.scandir(folder)]
# print(len(all_files2), perf_counter() - start)
# print(all_files == all_files2)

# ------------------------ os.path.
# abspath() — возвращает абсолютный путь;
# basename() — возвращает имя файла из абсолютного или относительного пути;
# dirname() — возвращает имя (путь) папки, в которой расположен файл;
# split() — делит путь к файлу на путь к папке и имя файла (заменяет вызов двух предыдущих функций);
# relpath() — определяет путь к файлу относительно другой папки, не обращается к реальной файловой системе,
#       чисто вычисления (полезна при сохранении путей к файлам в базе данных относительно заданного корня);
# join() — склеивает путь из частей (надеемся, вы не делаете это через строки!);
# exists() — проверяет существование объекта файловой системы.
# ------------------------

# --------------------- os.path.relpath

# root = r'C:\prog\Python3\Lib\site-packages\django'
# folder = r'C:\prog\Python3\Lib\site-packages\django\contrib\admin'
# django_admin_dirs = [
#     os.path.relpath(item, root)
#     for item in os.scandir(folder)
#     if item.is_dir() and not item.name.startswith('_')
# ]
# print(django_admin_dirs)

# --------------------- os.path.exists()
#
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# print('exists', os.path.exists(curr_file))

# # --------------------- os.path.split() всегда возвращает список из двух элементов
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# f_dir, f_name = os.path.split(curr_file)
# print(f_dir, f_name, sep=' | ')

# --------------------- os.path.dirname()
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# f_dir, f_name = os.path.split(curr_file)
# print('dirname ok', f_dir == os.path.dirname(curr_file))
# print(os.path.dirname(curr_file))

# --------------------- os.path.basename()
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# f_dir, f_name = os.path.split(curr_file)
# print('basename ok', f_name == os.path.basename(curr_file))
# print(os.path.basename(curr_file))

# --------------------- os.path.abspath()
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# print('abspath ok', curr_file == os.path.abspath(curr_file))
# print(os.path.abspath(curr_file))

# --------------------- os.path.relpath() + os.path.join()
# curr_file = r'C:\prog\Python3\Lib\site-packages\django\http\request.py'
# root = r'C:\prog\Python3\Lib\site-packages\django'
# curr_file_rel = os.path.relpath(curr_file, root)
# print(curr_file_rel)
#
# print('relpath ok', curr_file == os.path.join(root, curr_file_rel))

# ------------------------- переименование, создание и удаление папок
# ----------------- os.mkdir - для создания одной папки
# dir_name = 'sample_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# ----------------- os.makedirs - для создания папки в папке
# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)

# ----------------- os.rename - переименование папки ( можно и файлы)
# dir_name = 'first_out_dir'
# new_dir_name = 'first_new_dir'
# # new_dir_name = '../first_new_dir'
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)

# --------------------------- удаление файлов os.remove()
# to_remove_dir_name = 'apple.txt'
# if os.path.exists(to_remove_dir_name):
#     os.remove(to_remove_dir_name)

# --------------------------- удаление пустых папок os.rmdir()
# to_remove_dir_name = 'second_dir'
# if os.path.exists(to_remove_dir_name):
#     os.rmdir(to_remove_dir_name)
#     папка не пуста, не выйдет

# ---------------------- удаление не пустых папок
import shutil

# to_remove_dir_name = 'second_dir'
# if os.path.exists(to_remove_dir_name):
#     shutil.rmtree(to_remove_dir_name)
# shutil.
# copyfileobj() —  копирование одного файлового объекта в другой;
# copyfile() — копирование содержимого одного файла в другой (настройки доступа не копируются);
# copy() — копирование файла (копируются настройки доступа);
# copy2() -— копирование файла (копируются настройки доступа и метаданные — о них подробнее позже).

# ----------- copyfileobj()
# for _ in range(3):
#     with open('data/hello.txt', encoding='utf8') as src:
#         with open('data/summary.txt', 'a', encoding='utf8') as dst:
#             head_size = random.randrange(21)
#             print(head_size, src.read(head_size))
#             shutil.copyfileobj(src, dst)

# ------------------
# from shutil import copyfile, copy, copy2
# def show_stat(f_path):
#     stat = os.stat(f_path)
#     print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
#         f_p=f_path,
#         perm=oct(stat.st_mode),
#         m_t=stat.st_mtime,
#         a_t=stat.st_atime,
#     ))
#
#
# src = 'data/summary.txt'
# show_stat(src)
# show_stat(copyfile(src, 'new_data/summary_clone.txt'))
# show_stat(copy(src, 'new_data'))
# show_stat(copy2(src, 'new_data/summary_clone_2.txt'))

# ------------------
# from collections import defaultdict
# from os.path import relpath
#
# import django
#
# root_dir = django.__path__[0]
# django_files = defaultdict(list)
# for root, dirs, files in os.walk(root_dir):
#     for file in files:
#         ext = file.rsplit('.', maxsplit=1)[-1].lower()
#         rel_path = relpath(os.path.join(root, file), root_dir)
#         django_files[ext].append(rel_path)
#
# for ext, files in sorted(django_files.items(),
#                          key=lambda x: len(x[1]), reverse=True):
#     print(f'{ext}: {len(files)}')
#
# print('\nPY FILES')
# print(*sorted(django_files['py'])[:10], sep='\n')

# ------- директория, папки файлы отдельно
# root_dir = django.__path__[0]
# for root, dirs, files in os.walk(root_dir):
#    print(root, len(dirs), len(files))
# -------
#                                     использование обычного словаря
# django_files = {}
# root_dir = django.__path__[0]
# for root, dirs, files in os.walk(root_dir):
#     for file in files:
#         ext = file.rsplit('.', maxsplit=1)[-1].lower()
#         rel_path = relpath(os.path.join(root, file), root_dir)
#         if ext not in django_files:
#             django_files[ext] = []
#         django_files[ext].append(rel_path)
# print(django_files)

# ------------------------------ classwork

