from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.scrapethissite.com/pages/', UserAgent().random)

text = response.text
soup = BeautifulSoup(text, 'html.parser')
pages = soup.find_all('div', class_='page')

print(soup.title.text, '\n')
for page in pages:
    header = page.find('a').text
    subtitle = page.find('p', class_='lead').text.strip()   #возвращаемый текст заполнен пробелами -> удаляем
    print(f'Name: {header}\n{subtitle}\n\n')
