import requests, bs4
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
regexp_str = ''
for i in range(0, len(KEYWORDS)):
    KEYWORDS[i] = f'([{KEYWORDS[i][0]}{KEYWORDS[i][0].swapcase()}]{KEYWORDS[i][1:]})'
regexp_str = '|'.join(KEYWORDS)

KEYWORDS = set(KEYWORDS)
response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, features='html.parser')
articles_title_url_time = []
articles = soup.find_all('article')

for article in articles:
    article_title_text = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
    article_url_text = 'https://habr.com' + article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
    article_datetime_text = article.find(class_='tm-article-snippet__datetime-published').find('time').get('title')
    articles_title_url_time.append({'title': article_title_text, 'url': article_url_text, 'datetime': article_datetime_text})

for article in articles_title_url_time:
    response = requests.get(article['url'])
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    find_all_clothes = soup.find(class_='tm-article-presenter__content tm-article-presenter__content_narrow').find_all(text=re.compile(regexp_str))
    if find_all_clothes:
        print(f'{article["datetime"]} {article["title"]}  {article["url"]}')