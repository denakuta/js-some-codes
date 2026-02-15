from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

response = requests.get('https://quotes.toscrape.com/', UserAgent().random)

# print(response.status_code)
text = response.text
soup = BeautifulSoup(text, 'html.parser')
quotes = soup.find_all('div', class_='quote')
lst = ''

for quote in quotes:
    phrase = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = quote.find_all('a', class_='tag')
    print(f'{phrase[1:-1]}\n\nby: {author}\ntags: ', end='')
    for tag in tags:
        print(tag.text, end=' ')
    print('\n\n\n')
