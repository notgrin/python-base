"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml
 стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в
 любом текстовом редакторе «руками» (не программно);
  предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""
import os

folder1 = []
with open('config.yaml', 'r', encoding='utf8') as f:

    first_line = f.readline()
    first_line = first_line.strip().split('--')[1]
    for line in f:
        line = line.strip()
        line = line.split('--')
        a = len(line[0])
        if a == 1:
            folder1.append(line[1])


main_folder = first_line
folders_in_main_folder = folder1

for folder_name in folders_in_main_folder:
    dir_path = os.path.join(main_folder, folder_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)