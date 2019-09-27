import os
import shutil
import sys


# press 4
def create_dir(path):
    """ф-ция создания папки"""
    folder_path = os.path.join(os.getcwd(), path)

    try:
        os.mkdir(folder_path)
        print('Folder create successful =)')
    except:
        print(folder_path + ' - this folder is exists')


# press 1
def change_folder(path):
    """ф-ция перехода в указ. папку """
    try:
        os.chdir(path)
        print(os.getcwd() + ' - current folder')
    except:
        print(path + ' - folder is not exists')


# press 2
def list_folder(path):
    """ф-ция просмотра содержимого текущей папки"""
    for i in os.listdir(path):
        print(i)


# press 3

def delete_folder(path):
    """ф-ция удаления указ. папки"""
    folder_path = os.path.join(os.getcwd(), path)

    try:
        os.rmdir(folder_path)
        print('Folder delete successful =)')
    except:
        print(folder_path + ' - the folder is not exists')

