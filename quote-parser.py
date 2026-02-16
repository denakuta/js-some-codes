from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


def search(quotes):
    for quote in quotes:
        phrase = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = quote.find_all('a', class_='tag')

        print(f'{phrase[1:-1]}\n\nby: {author}\ntags: ', end='')

        for tag in tags:
            print(tag.text, end=' ')
        print('\n\n\n')


url = 'https://quotes.toscrape.com/'
headers = {"User-Agent": UserAgent().random}
curr_url = url

while curr_url:
    response = requests.get(curr_url, headers=headers)

    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    search(quotes)

    next_btn = soup.find("li", class_="next")

    if next_btn:
        relative_path = next_btn.a['href']
        curr_url = urljoin(curr_url, relative_path)
    else:
        curr_url = None
