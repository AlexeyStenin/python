# Задача-1:
# Напишите небольшую консольную утилиту,# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py


import os
import less05_easy_to_import


entry = ''
while entry != '0':
    print('*************MENU of possible action:*************')
    print('Go to Folder - select 1')
    print('Show content current folder - select 2')
    print('Delete Folder - select 3')
    print('Create folder - select 4')
    print('For exit - select 0')
    print('**************************************************')
    entry = input('Select: ')
    print(entry)
    if entry == '1':
        dir_name = input('insert full folder path: ')
        less05_easy_to_import.change_folder(dir_name)

    elif entry == '2':
        dir_name = os.getcwd()
        less05_easy_to_import.list_folder(dir_name)

    elif entry == '3':
        dir_name = input('insert full folder path: ')
        less05_easy_to_import.delete_folder(dir_name)

    elif entry == '4':
        dir_name = input('insert full folder path: ')
        less05_easy_to_import.create_dir(dir_name)

    elif entry == '0':
        print('You`re exit from MENU.')

    else:
        print('Action is impossible')



