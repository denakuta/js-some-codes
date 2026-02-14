from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests, subprocess

ua = UserAgent().random
response = requests.get('https://books.toscrape.com/', ua)

# if response.status_code == 200:
#     print('all OK')
# else:
#     print('something is wrong\n', response.status_code)

text = response.text
soup = BeautifulSoup(text, 'html.parser')
# print(soup.title.text)
books = soup.find_all('article', class_='product_pod')


def show_image(*args):
    subprocess.run(['kitty', 'icat', '--align', 'left', *args])
    return ''


for book in books:
    title = book.h3.a['title']
    img = book.div.a.img['src']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][-1]
    print(f'{show_image(f'https://books.toscrape.com/{img}')}\n\n{title}\n    price: {price}\n       ⭐: {rating} ')