# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Task 1
a = 3
b = 4
c = 'Task1'

print(a)
print(b)
print(c)


name = input('What is your name? - ')
print('Your name is ', name)


# Task 2
number = int(input('Введите, пожалуйста, число: '))
print(number+2)

# Task 3
age = int(input('Сколько Вам лет?  '))
if age < 18:
    print('Доступ несовершеннолетним запрещен!')
else:
    print('Добро пожаловать на ресурс!')
