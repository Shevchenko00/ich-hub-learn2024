# # Приветствие
# name = input("Введите свое имя: ")
# age = int(input("Введите сколько вам лет: "))
# print('Привет', name, "тебе", age, "лет!", "Тебе будет 30 через", int(30-age), "Лет")
# #Конец блока

# age = int(input("Your old: "))
# if age >= 18:
#     print('You are adult')
# else:
#     print('You are child')


# input('Напиши Python: ')
# print("Python is very interesting to learn")


# print("Понедельник = ('1	Python 1: Введение
# в язык программирования Python, установка среды разработк,
# Python 2: Основы работы с Python, Linux 1: Введение в Linux')")
# print('Вторник = Data and Databases 1:
# Основные понятия и базовый синтаксис выборки, German lesson 1 advanced (2)')
# # print('Среда = Python 3: Операторы,
# выражения, Python 4: Логический тип данных и сравнения, Linux 2: Первые команды')
# print('Четверг = Data and Databases 2:
# Более сложные инструменты выборки и правильный CodeStyle, Python 5: Условный оператор if, German: Разговорный клуб')
# print('Пятница = Python 6: Python Summary
# session 1, Data and Databases 3: Summary session 1. Linux 3: Практикум 1')


# name = input("Введите ваше имя: ")
# age = int(input("Введите сколько вам лет: "))
# print('Привет,', name, "тебе", age, "лет!")
# #Конец блока


# x = 5
# y = 2
#
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)

# pupils = int(input("Введите количество школьников: "))
# # apples = int(input("Введите количество яблок: "))
# #
# # print("Каждому школьнику досталось:", apples // pupils)
# # print("В корзине осталось: ", apples % pupils)


# days = int(input("Введите колисчество дней: "))
# hours = int(input("Введите колисчество часов: "))
# minutes = int(input("Введите колисчество минут: "))
# second = int(input("Введите колисчество секунж: "))
#
# print((days * 86400) + (hours * 3600 ) + (minutes * 60) + second))


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if id(a) == id(b) == id(c):
#     print(False)
# else:
#     print(True)


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Сумма: ", a + b)
# print('Разность: ', a - b)
# print("Произведение: ", a * b)
# print('Частное: ', a/b)
# print('Остаток от деления: ', a % b)
# print("Первое число в степени второго числа: ", a ** b)
# #

# pi = float(3.14159)
# r = float(input("Введите радиус окружности: "))
# long = 2 * pi * r
# area = (pi * r ** 2)
# print('Длинна окружности: ', long)
# print("Площадь окружности: ", area)


# x1 = float(input("Введите координату x1 первой точки: "))
# y1 = float(input("Введите координату y1 первой точки: "))
# x2 = float(input("Введите координату x2 второй точки: "))
# y2 = float(input("Введите координату y2 второй точки: "))
# dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print("Расстояние между точками: ", dist)

# first_value = input("Введите первое логическое значение (True или False): ").lower() == 'true'
# second_value = input("Введите второе логическое значение (True или False): ").lower() == 'true'
#
# result_and = first_value and second_value
# result_or = first_value or second_value
#
# first = not first_value
# second = not second_value
# equal = first_value == second_value
# not_equal = first_value != second_value
# print("Результат логического И:", result_and)
# print("Результат логического ИЛИ:", result_or)
# print("Результат логического НЕ (для первого значения):", first)
# print("Результат логического НЕ (для второго значения):", second)
# print("Результат сравнения на равенство:", equal)
# print("Результат сравнения на неравенство:", not_equal)


# a = int(input("Введите ваш возраст: "))
# if a >= 18:
#     print("Ты совершеннолетний")
# else:
#     print("Ты несовершеннолетний")


# it_rains = False
# if it_rains == True:
#     print("I will take my imbrella")
# else:
#     print("I will not take my umbrella")
#
# a = input("Введите погоду: ")
# if a == "Дождь":
#     print("Лучше надеть резиновую обувь")
# elif a == "Жарко":
#     print("Лучше надеть открытую обувь")
# elif a == "Идет легкий дождь":
#     print("Лучше надеть кроссовки")
# a = int(input("Введите число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a > b > c:
#     print(c, b, a)
# elif b > a > c:
#     print(c, a, b)
# elif c > b > a:
#     print(a, b, c)
# elif b > c > a:
#     print(a, c, b)
# elif a > c > b:
#     print(b, c, a)
# elif c > a > b:
#     print(b, c, a)
#
#
# years = int(input("Введите год: "))
# if years % 4 == 0 and years % 100 != 0 or (years % 400 == 0):
#     print("Год високосный!")
# else:
#     print("Год не високосный!")


# a = 6
# b = -81
# difference = a - b
# print("Разность между числами 6 и -81:", difference)


# a = input("Введите значение a (True или False):")
# b = input("Введите значение b (True или False):")
# if a == "True":
#     a = True
# if a == "False":
#     a = False
# if b == "True":
#     b = True
# if b == "False":
#     b = False
# print("a and b =", a and b)
# print("a or b =", a or b)
# print("not a =", not a)
# print("not b =", not b)
# print("a == b =", a == b)

# import struct
#
# num = float(input("Введите десятичное число: "))
# packed = struct.pack('>f', num)
# binary_str = ''.join(f'{byte:08b}' for byte in packed)
# print(f"Представление числа в формате IEEE 754: {binary_str}")

# Реализуйте алгоритм перевода числа в двоичную систему счисления, используя основные концепции представления чисел
# num = int(input("Enter a number: "))
# s = ""
# while num:
#     s += str(num % 2)
#     num //= 2
# print(s[::-1]) #CЛАЙС
# s1 = ''

# num = float(input("Введите число с плавающей точкой: "))
# round(num, 1)

# 1. Чисел в промежутке от 0 до 100

# i = 0
# s1 = 0
# s2 = 0
# s3 = 0
# s4 = 0
# while i <= 100:
#     s1 += i
#     if i % 3 == 0:
#         s2 += i
#     if i % 3 == 0 and i % 5 == 0:
#         s3 += i
#     if i % 3 == 0 or i % 5 == 0:
#         s4 += i
# print(s1)
# print(s2)
# print(s3)
# print(s4)


# i = 0
# s1 = 0
# s2 = 0
# s3 = 0
# s4 = 0
# while i <= 100:
#     s1 += i
#     if i % 3 == 0:
#         s2 += i
#     if i % 3 == 0 and i % 5 == 0:
#         s3 += i
#     if i % 3 == 0 or i % 5 == 0:
#         s4 += i
#     i += 1
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# import random
#
# mun = random.randint(1, 100)
# #Напишите программу, которая генерирует случайное
# число от 1 до 100, а затем предлагает пользователю угадать это число.
# while True:
#     num = int(input("Угадайте число от 1 до 100: "))
#     if num == mun:
#         break
#     if num < mun:
#         print('Число больше')
#     if num > mun:
#         print('Число меньше')


# num_fib = int(input("Enter the number: "))
#
# str_fib = [0, 1]
# index = 0
# index2 = 1
# #Напишите программу, которая запрашивает
# у пользователя число N и выводит первые N чисел
# Фибоначчи. Числа Фибоначчи - это последовательность
# чисел, где каждое следующее число является суммой двух
# предыдущих чисел (начиная с 0 и 1). Используйте цикл while
# для решения задачи. Выведите числа через запятую с помощью
# команды print.
# while len(str_fib) < num_fib:
#     num = str_fib.__getitem__(index) + str_fib.__getitem__(index2)
#     str_fib.append(num)
#     index += 1
#     index2 += 1
# #
# print(str_fib)
# #
# # #
#

# #Напишите программу, которая запрашивает у
# пользователя целое положительное число и проверяет,
# является ли оно простым. Простое число - это число,
# которое делится только на 1 и на само себя без остатка.
# Используйте цикл while и проверку деления числа на все числа
# от 2 до N-1 для решения задачи. Выведите соответствующее сообщение
# на экран с помощью команды print.
# n = int(input("Введите целое положительное число: "))
# if n < 2:
#     print(f"Число {n} не является простым.")
# else:
#     is_prime = True
#     i = 2
#     while i < n:
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1
#
#     if is_prime:
#         print(f"Число {n} является простым.")
#     else:
#         print(f"Число {n} не является простым.")

# Напишите программу, принимающую число с плавающей
# точкой и округляющую его до целого числа в соответствии
# с правилами школьной математики
# a = float(input("Введите число с плавающей точкой: "))
# print(int(round(a, 0)))


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(a ** b)
# print(a / b)


# a, b, c = int(input('Введите первое чиcло: ')),
# int(input('Введите второе чиcло: ')), int(input('
# Введите третье чиcло: '))
# if a > b:
#     print("Первое число больше второго")
# elif b > a:
#     print("Второе число больше первого")
# else:
#     print("Первое и второе числа равны")
# if a > c:
#     print("Первое число больше третьего")
# elif c > a:
#     print("Третье число больше первого")
# else:
#     print("Первое и третье числа равны")
# if b > c:
#     print("Второе число больше третьего")
# elif c > b:
#     print("Третье число больше второго")
# else:
#     print("Второе и третье числа равны")


# a, b, c = int(input('Введите первое чиcло: ')), int(input('Введите второе чиcло: '))
# if a > b:
#     print("Первое число больше")
# else:
#     print("Второе число больше")


# Для расчета гипотинузы(с округлением)
# first_catet = int(input("Первый катет: "))
# second_catet = int(input("Второй катет: "))
# sum = ((first_catet * first_catet + second_catet * second_catet) ** 0.5)
# print(round(sum, 2))


# a = bool(input("Первая улыбается?: "))
# b = bool(input("Вторая улыбается?: "))
# if a and b == input == True:
#  print("У нас проблемы")
# elif a and b == input == False:
#  print("У нас проблемы")
# else:
#  print("Все хорошо")


# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# if a != b:
#  print(f"Сумма {a + b}")
# elif a == b:
#  print(f"Числа одинаковые, удвоенная сумма: {(a + b)*2}")
# import math
# n = int(input("Введите первое число: "))
# a = int(input("Введите второе число: "))
# s = math.pi * math.pow(a, 2) / (4 * math.tan(math.pi/n))
# print(s)

# num = int(input("Введите целое число: "))
# orig= num
# revers = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = revers* 10 + digit
#     num = num // 10
# if original_num == revers:
#     print("Число является палиндромом")
# else:
#     print("Число не является палиндромом")

# text = str(input("Введите текст: "))
# alphabet = str(("abcdefghijklmnopqrstuvwxyz"))
# i = 1
# is_pangram = True
# text.lower()
# text.replace(" ", "")
# while i < len(alphabet):
#     if alphabet[i] not in text:
#         is_pangram = False
#         break
#     i += 1
# if is_pangram:
#     print("Строка является панграммой.")
# else:
#     print("Строка не является панграммой.")


# text = str(input("Введите текст: "))
# vowels = "aeiou"
# consonants = "bcdfghjklmnpqrstvwxyz"
# vowel_count = 0
# world_not_vowels = " "
# consonants_count = 0
# i = 1
# text.lower()
# text.replace(" ", "")
# while i < len(text):
#     char = text[i]
#     if char in vowels:
#         world_not_vowels
#     elif char in consonants:
#         consonants_count += 1
#     i += 1

# print("Количество гласных букв:", vowel_count)
# print("Количество согласных букв:", consonants_count)
#
#
#


# text = str(input("Введите предложение на русском: "))
# # sogl= ("бвгджзйклмнпрстфхцчшщъь")
# # glas = ("аеёиоуыэюя")
# # sogl_count = 0
# # glas_count = 0
# # text.lower()
# print(text.replace("б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, ъ, ь", ""))
# i = 0
# while i < len(text):
#     char = text[i]
#     if char in sogl:
#         sogl_count += 1
#     elif char in glas:
#         glas_count += 1
#
#     i += 1
#
# print("Количество гласных: ", glas_count)
# print("Количество согласных: ", sogl_count)

# a = input("Введите слово ").lower()
# glas = "aeuioy"
# i = 0
# while i < len(glas):
#     a = a.replace(glas[i], "")
#     i += 1
#
#
# print(a)


# a = input("Введите слово ").lower()
# symbols = ""
# repeated_symbols = ''
# i = 0
# while i <len(a):
#     if a[i] not in symbols:
#         symbols +=a[i]
#     else:
#         if a[i] not in repeated_symbols:
#             repeated_symbols += a[i]
#     i += 1
# print(repeated_symbols)


# a = input("Введите слово ").lower()
# glas = "aeuioy"
# i = 0
# while i < len(glas):
#     a = a.replace(glas[i], "")
#     i += 1
#
#
# print(a)


# a = input("Введите слово ").lower()
# symbols = ""
# repeated_symbols = ''
# i = 0
# while i <len(a):
#     if a[i] not in symbols:
#         symbols +=a[i]
#     else:
#         if a[i] not in repeated_symbols:
#             repeated_symbols += a[i]
#     i += 1
# print(repeated_symbols)


# user_string = input("Введите строку: ")
# width = int(input("Введите ширину: "))
# if len(user_string) > width:
#     print("Ширина меньше длины строки. Попробуйте снова.")
# else:
#     if width % 2 == 0:
#         centered_string = user_string.center(width)
#     else:
#         centered_string = user_string.center(width + 1)
#         centered_string = centered_string[:width]
#     print("Выравненная строка:")
#     print(centered_string)

# num = int(input("Введите целое число: "))
# original_num = num
# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num = num // 10
# if original_num == reversed_num:
#     print("Число является палиндромом.")
# else:
#     print("Число не является палиндромом.")
#
#
#
# num = input("Введите целое число: ")
# sum = 0
# i = len(num) - 1
# while i >= 0:
#     sum += int(num[i]) ** len(num)
#     i -= 1
#
# if sum == int(num):
#     print("Это число армстронга ")
# else:
#     print("Это не число армстронга")


# name = input("Введите имя и фамилию")
# sex = input("Пол и возpаст")
#
#
# while True:


# a = [1, 82, 74, 52,11]
#
# for i, a in enumerate(a):
#     print(i, a)
#


# 1.Задание (1 вариант)
# name = input("Введите ваше имя: ")
# age = input("Введите ваш возраст: ")
# live = input("Введите где вы живите: ")
#
# print(f"Привет {name}, тебе {age}, ты живешь в {live}")
# 1.Задание (2 вариант)
# name = input("Введите ваше имя: ")
# age = input("Введите ваш возраст: ")
# live = input("Введите где вы живите: ")
# text = "Привет {}, тебе {}, ты живешь в {}".format(name, age, live)
# print(text)
# 2.Задание
# first_number = float(input("Введите первое число: "))
# # second_number = float(input("Введите второе число: "))
# # sum = first_number + second_number
# # product = first_number * second_number
# # print(f"Сумма двух чисел {sum:.2}")
# # print(f"Произведение{product:.2}")

# text = input("Введите строку: ")
# tagname = input("Tagname: ")
# tag1 = f"<{tagname}> {text} </{tagname}>"
# print(tag1)
#
# input_str = input("Введите слово: ")
#
# last_two_chare = input_str[-2:]
# result = last_two_chare * 3
# print(result)

# a = input("ввдедите слово: ")
# print(a.find("f"))

# def my_len(str1, str2):
#     return len(f"{str1}{str2}")
#
#
# company1 = "apple"
# company2 = "samsumg"
#
# print(my_len(company1, company2))


# def greet_person(name, surname, greeting ="Hello", end_symbol= "!"):
#     print(greeting + name+ " " + surname)
#
# greet_person("Smith", "John",end_symbol="?", greeting="Hi")


# arr = list(range(1, 11))
#
#
# def func(i):
#     if i % 3 == 0 or i % 5 == 0:
#         return True
#     return False
#
#
# s = 0
# for j in arr:
#     if func(j):
#         s += j
# print(s)


# a = list(map(int, input().split()))
# print(a)
# unique_numbers = []
# for i in a:
#     if i not in unique_numbers:
#         unique_numbers.append(i)
# print(unique_numbers)
#


# DZZZ

# str = input()
# arr_str = str.split()
# new_str = arr_str[::-1]
# ' '.join(new_str)
#
# print(' '.join(new_str))

# 1. Напишите программу, которая принимает два числа и возвращает
# их сумму и произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print
# #Пример вывода:
#
# Введите первое число: 3
#
# Введите второе число: 4
#
# Сумма и произведение чисел: (7, 12)
# def func(a, b):
#     return a + b, a * b
#
#
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
#
# print(f"Cумма и произведение чисел: {func(a, b)}")

# 2. Напишите программу, которая принимает список чисел и возвращает сумму,
# минимальное и максимальное значение из списка. Используйте функцию для обработки
# списка чисел и возврата трех значений. Выведите результат на экран с помощью
# команды print.


# a = list(input("Напишите список чисел через пробел: ").split(","))
# a = list(map(int, a))
# big_number = max(a)
# low_number = min(a)
# sum_number = sum(a)
#
# print(f"Сумма равно {sum_number}")
# print(f"Максимальное {big_number}")
# print(f"Минимальное {low_number}")
# a = [66.25, 333, 333, 1234.5]
# a.insert(2, -1)
# a.remove(333)
# print(a, a.index(-1), a.count(333))
#


# import random
#
#
# def func(long_list, long_str):
#     for i in long_list:
#         index = random.randint(0, len(long_str))
#         long_str = long_str[:index] + str(i) + long_str[index:]
#     return long_str
#
#
# print(func([1, 2, 3], "Hello World"))

#
# a = int(input("Введите числа: "))
# print(min(a))

# def func():
#     a = 10
#     def in_func():
#         nonlocal a
#         a = 20
#     in_func()
#     print("Перменная внешней функции:", a)
#     func()


# def square(x):
#     return x ** 2
#
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)


# Напишите функцию, которая принимает список кортежей от
# пользователя, где каждый кортеж содержит информацию о студенте
# (имя, возраст, средний балл). Программа должна вывести на экран имена
# студентов, чей средний балл выше заданного значения. Используйте методы кортежей
# и циклы для обработки данных.Выведите итоговый список на экран с помощью
# команды print


# student = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
# n = int(input("Bведите минимальный средний балл: "))
# for student in student:
#     if student[2] >= n:
#         print(student[0])
# Напишите программу, которая принимает строку от пользователя
# и разбивает ее на отдельные слова. Затем программа должна создать
# новый кортеж, содержащий длину каждого слова в исходной строке.
# Используйте методы строк и кортежей для обработки данных
# user_input = input("Введите предложение: ")
# words = user_input.split()
# word_lengths = tuple(len(word) for word in words)
# print("Длины слов в предложении:", word_lengths)


# Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list,
# которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран. Объясните, почему изменения происходят только внутри функции и как работают
# изменяемые и неизменяемые параметры.


# def modify_list(num, spis):
#     for i in num:
#         if i % 2 == 0:
#             spis.append(i / 2)
#         else:
#             spis.append(i * 2)
#     return spis
#
#
# numbers = input("Введите числа: ").split()
# numbers = [int(n) for n in numbers]
# spisok = []
# modify_list(numbers, spisok)
# print(spisok)

# 2. Напишите программу, которая
# принимает произвольное количество аргументов от пользователя и передает
# их в функцию calculate_sum, которая возвращает сумму всех аргументов. Используйте
# оператор * при передаче аргументов в функцию. Выведите результат на экран.
#
# def calculate_sum(nums):
#     total_sum = 0
#     for i in nums:
#         total_sum += i
#     return total_sum
# nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print(calculate_sum(nufl;gkepgedfoiwfhios/

# def lru_cache(capacity, cache, key, value):
#     if key in cache:
#         cache.pop(key)
#     elif len(cache) >= capacity:
#         cache.popitem(last=False)
#     cache[key] = value

# capacity = 3
# cache = OrderedDict()
# lru_cache_with_params = partial(lru_cache, capacity, cache)
# print(cache)
# lru_cache_with_params(1, 2)
# print(cache)
# lru_cache_with_params(2, 3 )
# print(cache)
# lru_cache_with_params(3, 4)
# print(cache)
# lru_cache_with_params(4, 5)
# print(cache)

# from collections import defaultdict
#
# a = defaultdict()
# b = dict()
# with open('test.txt', 'r', encoding='utf-8') as file:
#     file = file.read().split()
#     print(file)
#     for word in file:
#         if word not in b:
#             b[word] = 0
#         else:
#             b[word] += 1
# print(b)

# fish_inventory = [
#     ("Sammy", "shark", 'tank-a'),
#     ("Jamie", "cuttlefish", "tank-b"),
#     ("mary", "squid", "tank-a"),
# ]
#
# tanks = defaultdict(list)
# for fish in fish_inventory:
#     tanks[fish[2]].append(fish[::2])
# print(tanks)
# print(tanks["tank-a"])
# print(tanks["tank-b"])
# print(tanks["tank-c"])


# def divide(x, y):
#     if y or x == 0:
#         raise ValueError('Деление на ноль не допустимо')
#     return x/y
# a = int(input("number1: "))
# b = int(input("number2: "))
# print(divide(a, b))

# def read_data(file_name):
#     data = []
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file.readline():
#             print(line)
#             fields = line.strip().split()
#             last_name = fields[0]
#             first_name = fields[1]
#             birth_year = int(fields[2])
#             course = fields[3]
#             score = fields[4]
#             data.append((last_name, first_name, birth_year, course, score))
#     return data
#
#
# file_name = 'test.txt'
# data = read_data(file_name)
# print(data)
# Напишите функцию merge_dicts, которая принимает произвольное
# количество словарей в качестве аргументов и возвращает новый словарь,
# объединяющий все входные словари. Если ключи повторяются, значения должны
# быть объединены в список. Функция должна использовать аргумент **kwargs для
# принятия произвольного числа аргументов словаря. Напишите функцию merge_dicts,
# которая принимает произвольное количество словарей в качестве аргументов и возвращает
# новый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны
# быть объединены в список. Функция должна использовать аргумент **kwargs для принятия
# произвольного числа аргументов словаря.

# def merge_dicts(**kwargs):
#     result = {}
#
#     for dictionary in kwargs.values():
#         for key, value in dictionary.items():
#             if key in result:
#                 if isinstance(result[key], list):
#                     result[key].append(value)
#                 else:
#                     result[key] = [result[key], value]
#             else:
#                 result[key] = [value]
#
#     return result
#
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'c': 5, 'd': 6}
# merged_dict = merge_dicts(dict1=dict1, dict2=dict2, dict3=dict3)
# print(merged_dict)

# Напишите программу, которая принимает
# строку от пользователя и подсчитывает
# количество уникальных символов в этой строке.
# Создайте функцию count_unique_chars, которая принимает с
# троку и возвращает количество уникальных символов. Выведите результат на экран.
# def count_unique_chars(s):
#     return len(set(s))
# input_string = input("Введите строку: ")
# unique_count = count_unique_chars(input_string)
# print("Количество уникальных символов:", unique_count)


# Напишите программу, которая создает словарь, содержащий информацию
# о студентах и их оценках. Ключами словаря являются имена студентов, а
# значениями - списки оценок. Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов и вычисляет средний балл для ка
# ждого студента. Функция должна возвращать новый словарь, в котором ключами явля
# ются имена студентов, а значениями - их средний балл. Выведите результат на экран.
# def calculate_average_grade(grades):
#     average_grades = {}
#     for student, grades_list in grades.items():
#         average_grades[student] = sum(grades_list) / len(grades_list)
#     return average_grades
# grades = {
#     'Alice': [85, 90, 92],
#     'Bob': [78, 80, 84],
#     'Carol': [92, 88, 95]
# }
# average_grades = calculate_average_grade(grades)
# print(average_grades)

# while True:
#     try:
#         surname, count = input("Input the vault the result: ").split()
#         count = int(count)
#         result[surname] += count
#     except:
#         print(result)
#         break
# my_generator = (x for x in range(10 + 1))
# for item in my_generator:
#     print(item)


# import itertools
#
# colors = ['red', 'green', 'blue']
# sizes = ['s', 'm', 'l']
# for colors, size in itertools.product(colors, sizes):
#     print(colors, size)

# def fmyrange(*args):
#     if len(args) > 3:
#         raise Exception('fmyrange accepts 3 arguments at most.')
#     if len(args) == 0:
#         raise Exception('fmyrange accepts at least one argument.')
#     if len(args) == 1:
#         begin, stop, increment = 0, args[0], 1
#     elif len(args) == 2:
#         begin, stop = args
#         increment = 1
#     else:
#         begin, stop, increment = args
#     i = begin
#     while (increment > 0 and i < stop) or (increment < 0 and i > stop):
#         yield i
#         i += increment

# from collections import Counter
# from collections import namedtuple
#
# from duplicity.config import action

# Напишите программу, которая подсчитывает количество вхождений каждого
# слова в тексте и выводит на экран наиболее часто встречающиеся слова. Для
# решения задачи используйте класс Counter из модуля collections. Создайте ф
# ункцию count_words, которая принимает текст в качестве аргумента и возвращает
# словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся
# слова и их количество.
# def count_words(text):
#     words = text.lower().split()
#     cleaned_words = [word.strip('.,!?;:') for word in words]
#     return Counter(cleaned_words)
#
# def most_common_words(word_counts, n=10):
#     return word_counts.most_common(n)
#
# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."""
#
# word_counts = count_words(text)
# common_words = most_common_words(word_counts)
#
# print("Наиболее часто встречающиеся слова:")
# for word, count in common_words:
#     print(f"{word}: {count}")

# Напишите программу, которая создает
# именованный кортеж Person для хранения
# информации о человеке, включающий поля name,
# age и city. Создайте список объектов Person
# и выведите информацию о каждом человеке на экран.
# person = namedtuple('Person', 'name age city')
# person1 = ('Alice', 25, 'New York')
# person3 = ('Bob', 30, 'London')
# person2 = ('Carol', 35, 'Paris')
# print(person1, '\n', person2, '\n', person3)


# Напишите программу, которая принимает словарь
# от пользователя и ключ, и возвращает значение
# для указанного ключа с использованием метода get
# или setdefault. Создайте функцию get_value_from_dict,
# которая принимает словарь и ключ в качестве аргументов,
# и возвращает значение для указанного ключа, используя метод
# get или setdefault в зависимости от выбранного варианта.
# Выведите полученное значение на экран.


# def get_value_from_dict(words, key, use_get_method):
#     if use_get_method == 'y':
#         return words.get(key)
#     else:
#         default_value = input('Введите значение по умолчанию: ')
#         return words.setdefault(key, default_value)
#
#
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# key = input("Введите ключ для поиска: ")
# use_get_method = input("Использовать метод get (y/n)? ")
# result = get_value_from_dict(my_dict, key, use_get_method)
# print(f"Значение для ключа '{key}': {result}")
#
# print(my_dict)
# Напишите программу, которая открывает
# файл, считывает из него два числа и
# выполняет операцию их деления. Если число
# отрицательное, выбросите исключение ValueError
# с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее
# сообщение.
# with open('text.txt', 'r') as text:
#     content = text.read()
#
# try:
#     numbers = content.split()
#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
#     result = num1 / num2
# except ValueError:
#     print('В текстовом файле при операции деления должны быть лишь положительные числа!'),
# else:
#     print("Результат деления:", result)


# Напишите программу, которая открывает файл,
# считывает его содержимое и выполняет операции над
# числами в файле. Обработайте возможные исключения при
# открытии файла (FileNotFoundError) и при выполнении операций
# над числами (ValueError, ZeroDivisionError). Используйте конструкцию
# try-except-finally для обработки исключений и закрытия файла в блоке finally.
# try:
#     file = open('text.txt', 'r')
#     content = file.read()
# except FileNotFoundError:
#     print(f"Файл не был найден в папке")
# try:
#     numbers = content.split()
#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Деление на ноль невозможно")
# except ValueError:
#     print('Введены некоректные данные')
# finally:
#     file.close()
#     print('Файл был закрыт. ')


# def generate_squares(n):
#     return (i * i for i in range(1, n + 1))
#
#
# n = int(input("Enter the number n: "))
#
# gen_sq = generate_squares(n)
# for square in gen_sq:
#     print(next(gen_sq))
# def word_multiply(a: str, b: int) -> str:
#     return a * b
#
#
# print(word_multiply("test", 3))
# from typing import Optional, Union, Any
#
#
# def greet(name: Optional [str]) -> Union [str, int]:
#     if name is None:
#         return "hello, anonymous"
#     else:
#         return f"Hello, {name}"
# b = greet('sema")

# Калькулятор от Aндрея
# import operator
#
# action = {
#     '+': operator.add,
#     '-': operator.sub,
#     '/': operator.truediv,
#     '*': operator.mul,
#     '**': operator.pow
# }
# equation = input().split()
# print(action[equation[1]](int(equation[0]), int(equation[2])))
# def list_str(a: list[str]) -> str:
#     return max(a, key=lambda s: len(s))
#
# print(list_str(["hello", "mama12312", "mia"]))
# Напишите функцию, которая принимает список словарей и ключ, по которому нужно отсортировать список словарей.
# Функция должна быть аннотирована с помощью аннотаций типов.
# dicts = [
#     {'age': 15, "name": 'Viktor'},
#     {'age': 23, "name": 'Tatyana'},
#     {'age': 45, "name": 'Olesya'}
# ]
#
# from operator import itemgetter
# from typing import Any
#
#
# def sort_list_of_dicts_by_key(people: list[dict], key: Any) -> list[dict]:
#     return sorted(people, key=itemgetter(key))
#
#
# print(sort_list_of_dicts_by_key(dicts,"name"))
# print(sort_list_of_dicts_by_key(dicts,"age"))


# 1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения.
# Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует генераторное выражение
# для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
# Пример работы программы:

# n = int(input("Enter the number : "))
# def generate_squares(n):
#     for i in range(1, n + 1):
#
#         yield i * i
# gen_sq = generate_squares(n)
# for i in range(n):
#     print(next(gen_sq))

# import time
#
#
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci()
#
# while True:
#     print(next(fib))
#     time.sleep(1)


# def my_generator(a, b):
#     if a == 0:
#         return print('exit')
#     else:
#         g = a + b
#         yield a
#         return print(g)
#
#
# n = int(input())
# c = int(input())
# print(my_generator(n, c))


# 1. Напишите генератор, который будет
# принимать на вход числа и возвращать
# их сумму. Генератор должен использовать
# инструкцию yield для возврата текущей суммы
# и должен продолжать принимать новые числа для
# добавления к сумме. Если генератор получает на вход
# число 0, он должен прекращать работу и вернуть окончательную
# сумму. Напишите программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.

# def sum_generator():
#     total = 0
#     while True:
#         value = yield total
#         if value == 0:
#             break
#         total += value
#     yield total
#
#
# gen = sum_generator()
# print(next(gen))
#
# while True:
#     user_input = int(input("Введите число (0 для завершения): "))
#     current_sum = gen.send(user_input)
#     print(f"Текущая сумма: {current_sum}")
#     if user_input == 0:
#         break
# #
# #
# def arithmetic_progression(start, step, count=None):
#     current = start
#     n = 0
#     while count is None or n < count:
#         yield current
#         current += step
#         n += 1
#
#
# start_value = int(input("Введите начальное значение: "))
# step_value = int(input("Введите шаг прогрессии: "))
# count_value = input("Введите количество элементов (или оставьте пустым для бесконечной прогрессии): ")
#
# if count_value.isdigit():
#     count_value = int(count_value)
# else:
#     count_value = None
#
# progression = arithmetic_progression(start_value, step_value, count_value)
#
# for value in progression:
#     print(value)
# Работа с файловой системой
# import sys
#
# print(f'Файл {}')
# print(sys.argv)
# print([arg for arg in sys.argv if arg[0] != '-'])


# with open('example.txt', 'r', encoding='utf-8') as input_file:
#     input_text = input_file.readline()
#     output_file1 = map(lambda x: x.lower(), input_text.split())
#     output_file2 = set(map(lambda x: ''.join(ch for ch in x if ch.isalpha() or ch == '-'), output_file1))
#     output_file3 = filter(lambda x: len(x) > 10, output_file2)
#     output_file3 = list(output_file3)
#     print(len(output_file3))
#     for word in output_file3:
#         print(word)

# 1
# def squared_num(lst:list) -> list:
#     result = []
#     for i in lst:
#         if i % 2 == 0:
#             result.append(i * i)
#     return result
#
#
# lts = []
#
# add = input('Введите значения для списка: ').split()
# lts = list(map(int, add))
#
# new_numbers = squared_num(lts)
#
# print("Исходный список:", lts)
# print("Квадраты чётных чисел:", new_numbers)
#
# #2
# from functools import reduce
#
# def compose_functions(functions, value):
#
#     return reduce(lambda acc, func: func(acc), functions, value)
#
# def add_one(x):
#     return x + 1
#
# def square(x):
#     return x * x
#
# def double(x):
#     return x * 2
#
# functions = [add_one, square, double]
# initial_value = 2
#
# result = compose_functions(functions, initial_value)
# print(result)


# 1
# def squared_num(lst:list) -> list:
#     result = []
#     for i in lst:
#         if i % 2 == 0:
#             result.append(i * i)
#     return result
#
#
# lts = []
#
# add = input('Введите значения для списка: ').split()
# lts = list(map(int, add))
#
# new_numbers = squared_num(lts)
#
# print("Исходный список:", lts)
# print("Квадраты чётных чисел:", new_numbers)
#
# #2
# from functools import reduce
#
# def compose_functions(functions, value):
#
#     return reduce(lambda acc, func: func(acc), functions, value)
#
# def add_one(x):
#     return x + 1
#
# def square(x):
#     return x * x
#
# def double(x):
#     return x * 2
#
# functions = [add_one, square, double]
# initial_value = 2
#
# result = compose_functions(functions, initial_value)
# print(result)
# import os
# import sys
# #
# arg = sys.argv
# if len(arg) < 2:
#     print('You should setup file name for running in cmd line')
# else:
#     name_file_for_run = arg[1]
#     os.system(f'python3 {name_file_for_run}')
#     print(arg)
# 1
# def squared_num(lst:list) -> list:
#     result = []
#     for i in lst:
#         if i % 2 == 0:
#             result.append(i * i)
#     return result
#
#
# lts = []
#
# add = input('Введите значения для списка: ').split()
# lts = list(map(int, add))
#
# new_numbers = squared_num(lts)
#
# print("Исходный список:", lts)
# print("Квадраты чётных чисел:", new_numbers)
#
# #2
# from functools import reduce
#
# def compose_functions(functions, value):
#
#     return reduce(lambda acc, func: func(acc), functions, value)
#
# def add_one(x):
#     return x + 1
#
# def square(x):
#     return x * x
#
# def double(x):
#     return x * 2
#
# functions = [add_one, square, double]
# initial_value = 2
#
# result = compose_functions(functions, initial_value)
# print(result)
#
# import os
# import sys


# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

# arg = sys.argv
# if len(arg) < 2:
#     print('You should setup file name for running in cmd line')
# else:
#     name_file_for_run = arg[1]
#     os.system(f'python3 {name_file_for_run}')
#     print(arg)

# Напишите программу, которая принимает в качестве аргумента
# командной строки путь к директории и выводит список всех файлов
# и поддиректорий внутри этой директории. Для этой задачи используйте модуль
# os и его функцию walk. Программа должна выводить полный путь к каждому файлу и директории.


# tree = os.walk(input('Введите путь к директории: '))
# print(tree)
#
# for i in tree:
#     print(i)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} {self.age}'
#
#
# mike = Person("Mike", 25)
# print(mike)
# Напишите программу, которая принимает список слов
# от пользователя и использует генераторное выражение
# (comprehension) для создания нового списка, содержащего
# только те слова, которые начинаются с гласной буквы. Затем
# программа должна использовать функцию map, чтобы преобразовать
# каждое слово в верхний регистр. В результате программа должна
# вывести новый список, содержащий только слова, начинающиеся с
# гласной буквы и записанные в верхнем регистре.
# name = input('Введите слова через пробел: ').split()  # Создаем список с словами от пользователя
# vowels = 'aeiou'
# modify_list = [word.strip() for word in name if
#                word.strip() and word.strip()[0].lower() in vowels]  # Создаем списковое включение
# # которое добавляет слова которые начинаются с большой буквы
# new_list = list(map(str.capitalize, modify_list))  # Переводит первую букву слова в верхний регистр
# print(new_list)
# Напишите программу, которая принимает список чисел
# от пользователя и использует функцию reduce из модуля
# functools, чтобы найти произведение всех чисел в списке.
# Затем программа должна использовать функцию itertools.accumulate
# для накопления произведений чисел в новом списке. В результате программа
# должна вывести список, содержащий накопленные произведения.
# from functools import reduce
# from itertools import accumulate
# numbers = input().split(',')
# numbers = list(map(int, numbers))
# sum_numbers = reduce(lambda x, y: x + y, numbers)
# accumulated_numbers = accumulate(numbers)
# print(list(accumulated_numbers))
# print(f'Сумма всех чисел {sum_numbers}')
# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота),
# а также метод calculate_area(), который вычисляет площадь прямоугольника.
# Затем создайте экземпляр класса Rectangle с заданными значениями ширины и высоты и выведите его площадь.
# class Rectangle:  # Создаем класс и назначаем высоту и ширину
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):  # Добавляем метод класса
#         return self.width * self.height
#
#
# sum_rectangle = Rectangle(1, 20)  # Задаем значение для вычисление площади
#
# sum_rectangle.calculate_area()  # Выводим результат

#
# Cоздать класс окружности, определить методы
# для площади и длины окружности


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __str__(self):
#         return f'Circle R={self.radius}'
#
#     def __repr__(self):
#         return f'Circle R={self.radius}'
#
#     def calc_square(self):
#         return 3.14 * self.radius ** 2
#
#     def calc_lenght(self):
#         return 2 * 3.14 * self.radius
#
#
# list_my_circle_1 = [Circle(randint(1, 10)) for x in range(10)]
# print(list_my_circle_1)
# max_circle = max(list_my_circle_1, key=lambda c: c.radius)
# print(list_my_circle_1.index(max_circle))


# ДЕКОРАТОРЫ /\/\/\/\/\/\/\/\/\/\/\


# def decorator(func):
#     def wrapper():
#         print('Сейчас выполним функцию')
#         func()
#         print('Функция выполнена')
#
#     return wrapper
#
#
# @decorator
# def my_func():
#     a, b = input('Введите слово').split()
#     print('Вот они', b, a)
#

import time

# def decorator(funk):
#     def wrapper():
#         start_time = time.time()
#         funk()
#         def_time = time.time() - start_time
#         print(def_time)
#
#     return wrapper
#
#
# @decorator
# def func():
#     for i in range(101):
#         print(i)
#
#
# func()
# class Person:
#     def __init__(self, height, weight, birth_year):
#         self.height = height
#         self.weight = weight
#         self.birth_year = birth_year
#
#     def __add__(self, other):
#         avg_height = ((self.height + other.height) / 2) / 4
#         avg_weight = ((self.weight + other.weight) / 2) / 20
#         birth_year = 2024
#         return Person(avg_height, avg_weight, birth_year)
#
#     def __str__(self):
#         return str(self.weight) + ' ' + str(self.height) + ' ' + str(self.birth_year)
#
#     def __len__(self):
#         return round(self.height)
#
#     def __bool__(self):
#         if self.weight > 0:
#             return True
#         else:
#             return False
#
#
# dad = Person(180, 70, 1982)
# mom = Person(174, 60, 1984)
# baby = dad + mom
# print(len(baby), baby)
# print(bool(baby))

# Напишите декоратор validate_args,
# который будет проверять типы аргументов функции и
# выводить сообщение об ошибке, если переданы аргументы
# неправильного типа. Декоратор должен принимать ожидаемые
# типы аргументов в качестве параметров.
from functools import wraps

# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args):
#             for arg, arg_type in zip(args, types):
#                 if not isinstance(arg, arg_type):
#                     raise TypeError(f"Argument {arg} has incorrect type {type(arg)}. Ожидается {arg_type}.")
#             return func(*args)
#
#         return wrapper
#
#     return decorator
#
#
# @validate_args(str, int)
# def function(name, age):
#     return f'Name {name}, age {age}'
#
#
# try:
#     print(function('Ivan', '34'))
# except TypeError as e:
#     print(e)
#
# # Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции
# # в лог-файл. Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>,
# # Результат: <результат>". Используйте модуль logging для записи в лог-файл.
# import logging
#
# logging.basicConfig(filename="log.txt", level=logging.INFO)
#
#
# def log_args(func):
#     def wrapper(*args):
#         result = func(*args)
#         logging.info(f'Результат: {result}, Аргументы: {args}')
#         return result
#
#     return wrapper
#
#
# @log_args
# def add(a, b):
#     return a + b
#
#
# add(2, 3)
# add(5, 7)
# path_input = input()
# for dir, i, files in os.walk(path_input):
#     for file in files:
#         print(file)
#     print(dir)


# #1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
#
# # - Увеличение значения счетчика на заданное число (оператор +=)
# #
# # - Уменьшение значения счетчика на заданное число (оператор -=)
# #
# # - Преобразование счетчика в строку (метод __str__)
# #
# # - Получение текущего значения счетчика (метод __int__)
# #
#
# class Counter:
#     def __init__(self, number=0):
#         self.number = number
#
#     def __add__(self, other):
#         self.number += other
#         return self
#
#     def __sub__(self, other):
#         self.number -= other
#         return self
#
#     def __int__(self):
#         return self.number
#
#     def __str__(self):
#         return f'{self.number}'
#
#
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6
#
# #2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
#
# # - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# #
# # - Преобразование письма в строку (метод __str__)
# #
# # - Получение длины текста письма (метод __len__)
# #
# # - Получение хеш-значения письма (метод __hash__)
# #
# # - Проверка наличия текста в письме (метод __bool__)
# class Email:
#     def __init__(self, out_of, to, subject, text, date):
#         self.out_of = out_of
#         self.to = to
#         self.subject = subject
#         self.text = text
#         self.date = date
#
#     def __len__(self):
#         return len(self.text)
#
#     def __hash__(self):
#         return hash(Email)
#
#     def __bool__(self):
#         return bool(Email)
#
#     def __lt__(self, other):
#         return self.date < other.date
#
#     def __gt__(self, other):
#         return self.date > other.date
#
#     def __le__(self, other):
#         return self.date <= other.date
#
#     def __eq__(self, other):
#         return self.date == other.date
#
#     def __ne__(self, other):
#         return self.date != other.date
#
#     def __ge__(self, other):
#         return self.date >= other.date
#
#     def __str__(self):
#         return f'From: {self.out_of}\nTo: {self.to}\nSubject: {self.subject}\n\n{self.text}'
#
#
# email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
#                "2022-05-10")
#
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
#
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
#
# print(len(email2))  # 24
#
# print(hash(email3))  # 5893289150385
#
# print(bool(email1))  # True
#
# print(email2 > email3) #True
#
# print(email3 > email2)#False
#
# print(email1 <= email2) #True
#
# print(email2 == email1) #True
#
# print(email2 != email1) #False
#
# print(email3 <= email2) #True


# import abc
#
#
# class Employee:
#     company = 'ABC company'
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     @classmethod
#     def set_company(cls, company_name):
#         cls.company = company_name
#
#     def get_info(self):
#         return f'Name: {self.name}\nPosition: {self.position}\nCompany: {self.company}'
#
#
# employee1 = Employee("John", "Manager")
#
# employee2 = Employee("Alice", "Developer")
#
# print(employee1.get_info())  # Вывод:
#
# Employee.set_company("XYZ Company")
#
# print(employee2.get_info())  # Вывод:
#
#
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self):
#         pass
#
#     @abc.abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * 3.14
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
#
# rectangle = Rectangle(5, 3)
# circle = Circle(2)
#
# print(f"Rectangle area: {rectangle.area()}")
# print(f"Rectangle perimeter: {rectangle.perimeter()}")
# print(f"Circle area: {circle.area()}")
# print(f"Circle perimeter: {circle.perimeter()}")

# Напишите функцию extract_emails(text),
# которая
# извлекает все адреса электронной почты из заданного
# текста и возвращает их в виде списка.

import re

#
# def extract_emails(text):
#     pattern = r'\b\w*@\w*\b'
#     return re.findall(pattern, text)
#
#
# text = "Contact us at info@example.com or support@example.com for assistance."
#
# emails = extract_emails(text)
#
# print(emails)

#
# Напишите функцию highlight_keywords(text, keywords),
# которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при
# поиске ключевых слов.


import re

# def highlight_keywords(text, keywords):
#     for word in keywords:
#         pattern = rf'\b{word}\b'
#
#         def add_symbol(match):
#             return f"*{match.group(0)}*"
#
#         text = re.sub(pattern, add_symbol, text, flags=re.IGNORECASE)
#
#     return text
#
#
# text1 = "This is a sample text. We need to highlight Python and programming."
# keyword = ["Python", "programming"]
# highlighted_text = highlight_keywords(text1, keyword)
#
# print(highlighted_text)


# import requests
# import re
# from collections import Counter
#
# #Напишите функцию extract_emails(text), которая
# # извлекает все адреса электронной почты из заданного
# # текста и возвращает их в виде списка.
# def get_response(url):
#     response = requests.get(url)
#     return f'Status Code: {response.status_code}\nResponse Text: {response.text}\nResponse Headers: {response.headers}'
#
#
# print(get_response('https://lms.itcareerhub.de/'))
#
#
#
# #Напишите функцию highlight_keywords(text, keywords),
# # которая выделяет все вхождения заданных ключевых слов в
# # тексте, окружая их символами *. Функция должна быть
# # регистронезависимой при поиске ключевых слов.
# def find_common_words(url_list):
#     all_words = []
#     for url in url_list:
#         try:
#             response = requests.get(url)
#             content = response.text
#             words = re.findall(r'\b\w+\b', content.lower())
#             all_words.extend(words)
#         except requests.RequestException as e:
#             print(f"Ошибка при обращении к {url}: {e}")
#     word_counts = Counter(all_words)
#     most_common_words = word_counts.most_common()
#     return most_common_words
#
#
# # Пример использования
# url_list = [
#     'https://ilibrary.ru/text/436/p.2/index.html',
#     'https://ilibrary.ru/text/69/p.4/index.html'
# ]
# top_words = find_common_words(url_list)
# print(top_words)
