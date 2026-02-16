from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": UserAgent().random}
response = requests.get('https://quotes.toscrape.com/', headers=headers)

text = response.text
soup = BeautifulSoup(text, 'html.parser')
quotes = soup.find_all('div', class_='quote')


def search():
    for quote in quotes:
        phrase = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = quote.find_all('a', class_='tag')
        print(f'{phrase[1:-1]}\n\nby: {author}\ntags: ', end='')
        for tag in tags:
            print(tag.text, end=' ')
        print('\n\n\n')

search()

try:
    while True:
        next_btn = soup.find("li", class_="next")
        response = requests.get(f'https://quotes.toscrape.com/{next_btn.a['href']}', headers=headers)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        search()
except AttributeError:
    print('\n\nQuotes ended!')