import requests

from bs4 import BeautifulSoup

import time


def extract():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    return soup


books = []
def transform(soup):
    ol = soup.find('ol')
    articles = ol.find_all('article', class_ = "product_pod")
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_= 'price_color').text
        price = float(price[1:])
        books.append([title,star,price])
    return books


c = extract()
print(transform(c))

