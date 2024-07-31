import requests
from bs4 import BeautifulSoup

#    Напишите программу, которая запрашивает у
#    пользователя URL-адрес веб-страницы, использует
#    библиотеку Beautiful Soup для парсинга HTML и
#    выводит список всех ссылок на странице.

# insert = input('Введите сайт: ')
# html = requests.get(insert).text
# soup = BeautifulSoup(html, "html.parser")
#
# links = soup.find_all('a')
# for link in links:
#     href = link.attrs.get('href')
#     if href[:4] == 'http':
#         print(href)
# Напишите программу, которая запрашивает у пользователя
# URL-адрес веб-страницы и уровень заголовков, а затем
# использует библиотеку Beautiful Soup для парсинга HTML и
# извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.)
# с их текстом.
# into = input('Введите название сайта и уровень заголовков через запятую: ').split(', ')
# html = requests.get(into[0]).text
# soup = BeautifulSoup(html, "html.parser")
#
# links = soup.find_all(str(into[1]))
# for link in links:
#     print(links)
