from fake_useragent import UserAgent
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='Scrape quotes from quotes.toscrape.com')
parser.add_argument("--pages", type=int)
parser.add_argument("--tag", type=str)

args = parser.parse_args()

lst = []


def search(quotes):
    for quote in quotes:
        phrase = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = quote.find_all('a', class_='tag')

        for tag in tags:
            lst.append(tag.text)
        if args.tag != None:
            if args.tag in lst:
                print(f'{phrase[1:-1]}\n\nby: {author}\ntags:', ', '.join(lst), end='')
                print('\n\n\n')
        else:
            print(f'{phrase[1:-1]}\n\nby: {author}\ntags: ', ', '.join(lst), end='')
            print('\n\n\n')
        lst.clear()


url = 'https://quotes.toscrape.com/'
headers = {"User-Agent": UserAgent().random}
curr_url = url

counter = 0
while curr_url:
    counter += 1
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

    if args.pages:
        if counter >= args.pages:
            break
