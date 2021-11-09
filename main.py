import requests, bs4
import re
KEYWORDS = ['штраф']
#KEYWORDS = ['дизайн', 'фото', 'web', 'python']
for k in KEYWORDS:
    temp = ''
    if k[0].isalpha():
        temp
    k = f'([{k[0]}{k[0].swapcase()}]{k[1:]}'
#TODO: переработать в заготовку для регекспа
KEYWORDS = set(KEYWORDS)
response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, features='html.parser')
articles_title_url_time = []

articles = soup.find_all('article')
# article_title_text = articles[0].find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
# article_url_text = 'https://habr.com' + articles[0].find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
# article_datetime_text = articles[0].find(class_='tm-article-snippet__datetime-published').find('time').get('title')

# print(article_title_text)
# print(article_url_text)
# print(article_datetime_text)
# print(articles[0])

for article in articles:
    article_title_text = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
    article_url_text = 'https://habr.com' + article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
    article_datetime_text = article.find(class_='tm-article-snippet__datetime-published').find('time').get('title')
    articles_title_url_time.append({'title': article_title_text, 'url': article_url_text, 'datetime': article_datetime_text})

for article in articles_title_url_time:
    response = requests.get(article['url'])
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    find_all_clothes = soup.find_all(text=re.compile("([Pp]ython)"))
    if find_all_clothes:
        print('да')
    else:
        print('нет')