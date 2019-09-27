# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# C:\Users\Alex\PycharmProjects\lesson05\easy.py
# path_name = 'C:\\Users\\Alex\\PycharmProjects\\lesson05\\'

# импорт ко всем заданиям.


import os
import shutil
import sys

# Task1
# create
for i in range(1, 10):
    os.mkdir('DIR_' + str(i))

# del
for i in range(1, 10):
    os.rmdir('DIR_' + str(i))

# Task2 show only FOLDERS in current folder

print('Списком')
cur_folders = [i for i in os.listdir() if os.path.isdir(i)]
print(cur_folders)
#
print('или в Столбец')
for i in os.listdir():
    if os.path.isdir(i) is True:
        print(i)


# Task3 shutil copy(src, dst)

my_file = sys.argv[0]
copy_my_file = my_file + '_copy'
shutil.copy(my_file, copy_my_file)


