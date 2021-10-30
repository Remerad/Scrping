import requests, bs4
#KEYWORDS = ['Python']
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

KEYWORDS = set(KEYWORDS)
response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.find('span').text for hub in hubs)
    if KEYWORDS & hubs:
        href = article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
        link = 'https://habr.com' + href
        tm = article.find(class_ = 'tm-article-snippet__datetime-published').text
        print(tm, '-', article.find('h2').text, '-', link)
