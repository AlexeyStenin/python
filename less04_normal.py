# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1 Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны
# иметь заглавные первые буквы. email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем
# регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или
# com. Например: Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол,
# заглавная буква, .net), te_4_st@test.com - верно указан.

# Task1

import re

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')

pattern_name = pattern_surname = '^[А-ЯA-Z]{1,1}'               # ^ - start of string; [А-Я] word of range; {} position
if (re.match(pattern_name, name) and re.match(pattern_surname, surname)) is not None:
    print(name + ' ' + surname)
else:
    print('Вы ввели неверные данные =(')

e_mail = input('Введите ваш электронный адрес: ')
pattern_email = '[a-z_0-9]+@+[a-z0-9]+\.(ru|com|org)'
if re.match(pattern_email, e_mail) is not None:
    print(e_mail)
else:
    print('Вы ввели неверный e-mail =(')

