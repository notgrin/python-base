"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей
 структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
 как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять
  имена папок под конкретный проект;
   можно ли будет при этом расширять конфигурацию и хранить данные о вложенных
    папках и файлах (добавлять детали)?
"""
import os

main_folder = 'my_project'
folders_in_main_folder = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder_name in folders_in_main_folder:
    dir_path = os.path.join(main_folder, folder_name)
    if not os.path.exists(dir_path):    # проверка, если папка уже существует
        os.makedirs(dir_path)
