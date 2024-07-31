# number1 = int(input("введите первое число: "))
# number2 = int(input("введите второе число: "))
# plus = number1 + number2
# umnoz = number1 * number2
# print(f"Сумма чисел равна:  {plus}, произведение равно: {umnoz}")
# weight = int(input("Введите длину прямоугольнака: "))
# height = int(input("Введите ширину прямоугольника: "))
# print(f"Периметр треугольника {weight * 2 + height * 2} ")
# c = int(input("Введите температуру в цельсиях: "))
# f = float(c * 9/5 + 32)
# print(f)
# number = int(input("Введите число: "))
# if number >= 0:
#     print("Число положительное")
# else:
#     print("Число отрицательное")
# from collections import defaultdict


# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
# age = int(input("Введите ваш возраст: "))
# if age <= 13:
#     print("Вы еще ребенок")
# elif age <= 19:
#     print("Вы подросток")
# else:
#     print("Вы уже взрослый")


# number = int(input("enter: "))
# i = 0
# sum = [0, 1]
# k = 1
# while len(sum) < number:
#     n = sum.__getitem__(i) + sum.__getitem__(k)
#     sum.append(n)
#     i += 1
#     k += 1
# print(sum)


# numbers = int(input("Введите число: "))
#
# result = ""
#
# for i in range(1, numbers + 1 ):
#     num = numbers * i + 1
#     for j in range(i, num, i):
#         if j < num - 1:
#             print(j, end="")
#         else:
#             print(j)

# def func_factorial(number):
#     factorial = 1
#     for i in range(2, number + 1):
#         factorial = i * factorial
#
#     return factorial
#
# print(func_factorial(int(input("Введите число: "))))

# def numbers():
#     for i in range(5):
#         text = int(input("Enter the number: "))
#         with open("test.txt", "a+") as file:
#             file.write(str(text))
# numbers()

# def transform(line):
#     line = line.split()
#     for i, word in enumerate(line):
#         if len(word) == 3:
#             line[i] = word.upper()
#     print(''.join(line))
#
# transform("the quicck brown fox jumps over the lazy doh")

# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# a = ['cat', 'dog', 'tac', 'god', 'act']
# def return_anagram_dict(words: list[str]):
#     word_dict = dict()
#     words = [(worщd, ".join(sorted(list(word)))) for word in words]


# Дано
# натуральное число N.  Написать функцию digits_sum(N),
# которая вычисляет сумму его цифр. При решении этой задачи
# пользуемся рекурсией, а строки, списки, массивы и циклы не используем.

# def digits_sum(n):
#     if n == 0:
#         return n
#     else:
#         return digits_sum(n // 10) + n % 10
#
#
# print(digits_sum(1234))
#
# result = defaultdict(int)
# while True:
#     try:
#         surname, count = input("Input the vault the result: ").split()
#         count = int(count)
#         result[surname] += count
#     except:
#         print(result)
#         break
# try:
#     x = int(input('Введите число:'))
#     x += 5
#     print(x)
# except ValueError:
#     print("Введите лучше число!")
#
# def generator(n):
#     pr = 0
#     while True:
#         pr = pr + n
#         yield pr
#         if n == 0:
#             return print('Программа завершила работу!')
#
#
# a = int(input("Введите число"))
# print(generator(a))

#
# class NoNameException(Exception):
#     pass


# class InvalidIbanException(Exception):
#     pass
#
# def is_valid_iban(iban):
#     return len(iban) > 15 and len(iban) < 34 and iban.isallnull()
#
#
# def validateCustomers(customers):
#     error_map = {}
#     try:
#         for first_name, last_name, birthdate, iban in customers
#             error = []
#             if not first_name:
#                 raise NoNameException("Имя не должно быть пустым")
#             if not last_name:
#                 raise NoNameException('Фамилия не должна быть пустой')
#             if not is_valid_iban:
#                 raise InvalidIbanException('Не кореректный ибан')
# class Car:
#     def __init__(self, model, year, color):
#         self.color = color
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return f'{self.color}, {self.model}, {self.year}'
#
#
# car1 = Car('toyota', 2003, 'green')
# car2 = Car('mercedes', 2011, 'white')
# car3 = Car('porsche', 2020, 'yellow')
# car4 = Car('audi', 2000, 'black')
# car5 = Car('pegout', 2019, 'blue')
# car6 = Car('ford', 2005, 'blue')
# car7 = Car('Rolls-Royce', 2021, 'gray')
# car8 = Car('Opel', 2022, 'braun')
# car9 = Car('BMW', 1991, 'yellow')
# car10 = Car('Renault', 2024, 'green')
# car_list = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
#
#
# def car_func(list_car, color_car):
#     result = filter(lambda x: x.color == color_car, list_car)
#     return list(result)
#
#
# for car in car_func(car_list, 'blue'):
#     print(car)
# from datetime import datetime
#
#
# class Person:
#     def __init__(self, name, birthday):
#         self.name = name
#         self.birthday = birthday
#
#
# people1 = Person('Nikita', '23.02.2000')
# people2 = Person('Oleh', '10.01.1982')
# people3 = Person('Gennadiy', '29.09.1939')
# people4 = Person('Nataliya', '01.01.2020')
# people5 = Person('Nadya', '21.06.2001')
# people6 = Person('Oleksandr', '01.02.2004')
# people_list = [people1, people2, people3, people4, people5, people6]
#
#
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name}, {self.age}'
#
#
#     def get_age(self, age):
#         self.age = age
#
# def age_people(people_list):
#     for p in people_list:
#         age1 = (datetime.now().year - (datetime.strptime(p.birthday, '%d.%m.%Y').year))
#         print(f'{p.name}, {age1} year')
#
#
# Employee(name, age_people(people_list))
# age_people(people_list)
#
# Генерация списка номеров телефонов
# phone_numbers = [
#     "+1-800-555-0199",
#     "+1-800-555-0175",
#     "+44-20-7946-0958",
#     "+44-20-7946-0347",
#     "+49-30-1234567",
#     "+49-30-2345678",
#     "+33-1-40406050",
#     "+33-1-50506070",
#     "+7-495-123-4567",
#     "+7-495-234-5678"
# ]
#
# # Импортируем модуль re для работы с регулярными выражениями
# import re
#
# # Регулярное выражение для парсинга международных номеров телефонов
# phone_regex = re.compile(r'\+(\d{1,3})-(\d{1,4})-(\d{3,4})-(\d{4,7})')
#
# # Парсинг и вывод номеров телефонов
# for number in phone_numbers:
#     match = phone_regex.match(number)
#     if match:
#         country_code, area_code, prefix, line_number = match.groups()
#         print(f"Country Code: {country_code}, Area Code: {area_code}, Prefix: {prefix}, Line Number: {line_number}")
#     else:
#         print(f"Number {number} is not valid.")
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
# print(counter)
# counter -= 2
# print(counter)
# import requests
# import sys
#
#
# #
# # #
# arg = sys.argv
# if len(arg) < 2:
#     print('You should setup website name for running')
# else:
#     name_site_for_run = arg[1]
#
# response = requests.get(f'{name_site_for_run}')
# if response.status_code == 200:
#     print('The website is available')
# else:
#     print('The website is not available')
#

# def weather(latitude, longitude):
#     website = requests.get(
#         f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
#     return website.json
#
#
# print(weather(3.13, 9.19))

# Изучите API ресурса http://www.boredapi.com/
# Напишите программу, которая запрашивает у пользователя, чем он хотел
# бы заняться, и сколько всего будет участников, и с помощью изученного
# API предлагает вариант активности.

#
# import mysql.connector
#
# class Connector:
#     def get_connect(database='ich_edit'):
#         dbconfig = {
#             'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#             'user': 'ich1',
#             'password': 'password',
#             'database': database,
#     }
#     connection = mysql.connector.connect(**dbconfig)
#     cursor = connection.cursor()
#         return cursor, connection