import requests
import re
from collections import Counter

#Напишите функцию extract_emails(text), которая
# извлекает все адреса электронной почты из заданного
# текста и возвращает их в виде списка.
def get_response(url):
    response = requests.get(url)
    return f'Status Code: {response.status_code}\nResponse Text: {response.text}\nResponse Headers: {response.headers}'


print(get_response('https://lms.itcareerhub.de/'))



#Напишите функцию highlight_keywords(text, keywords),
# которая выделяет все вхождения заданных ключевых слов в
# тексте, окружая их символами *. Функция должна быть
# регистронезависимой при поиске ключевых слов.
def find_common_words(url_list):
    all_words = []
    for url in url_list:
        try:
            response = requests.get(url)
            content = response.text
            words = re.findall(r'\b\w+\b', content.lower())
            all_words.extend(words)
        except requests.RequestException as e:
            print(f"Ошибка при обращении к {url}: {e}")
    word_counts = Counter(all_words)
    most_common_words = word_counts.most_common()
    return most_common_words


# Пример использования
url_list = [
    'https://ilibrary.ru/text/436/p.2/index.html',
    'https://ilibrary.ru/text/69/p.4/index.html'
]
top_words = find_common_words(url_list)
print(top_words)
