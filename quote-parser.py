from fake_useragent import UserAgent
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests, argparse, time, json

start = time.time()

parser = argparse.ArgumentParser(description='Scrape quotes from quotes.toscrape.com')
parser.add_argument(
    "--pages",
    '-p',
    type=int,
    help='Enter the number of pages'
)
parser.add_argument(
    "--tag",
    '-t',
    type=str,
    help='Filter for tags'
)
parser.add_argument(
    '--output',
    '-o',
    type=str,
    help='Save to JSON'
)

args = parser.parse_args()




def search(quotes):
    result = []

    for quote in quotes:
        phrase = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = quote.find_all('a', class_='tag')
        lst = []

        for tag in tags:
            lst.append(tag.text)
        if args.tag:
            if args.tag not in lst:
                continue

        data = {
            "text": phrase,
            "author": author,
            "tags": lst
        }

        result.append(data)

    return result


url = 'https://quotes.toscrape.com/'
headers = {"User-Agent": UserAgent().random}
curr_url = url
quotes = []
counter = 0
all_quotes = []


pages_bar = tqdm(
    desc="Pages",
    unit=" pages",
    position=0,
)

quotes_bar = tqdm(
    desc="Quotes found",
    unit=' quotes',
    position=1)



while curr_url:
    counter += 1
    response = requests.get(curr_url, headers=headers)

    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')



    found = search(quotes)
    all_quotes.extend(found)

    quotes_bar.update(len(found))
    pages_bar.update(1)

    next_btn = soup.find("li", class_="next")

    if next_btn:
        relative_path = next_btn.a['href']
        curr_url = urljoin(curr_url, relative_path)
    else:
        curr_url = None

    if args.pages:
        if counter >= args.pages:
            break


if args.output:
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(all_quotes, f, indent=4, ensure_ascii=False)
    print(f'Saved {len(quotes)} quotes to {args.output}')
else:
    for q in all_quotes:
        print(f'{q['text'][1:-1]}\n\nby: {q['author']}\ntags:{', '.join(q['tags'])}\n\n', end='')


print(f'Scraping in {time.time() - start:.2f}s')
