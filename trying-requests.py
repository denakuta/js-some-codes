import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent().random
header = {'user-agent': ua}

link = 'https://browser-info.ru/'
response = requests.post(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find_all('div', id="cookie_check")
cookie_check = block[0].find_all('span')[1].text
result_cookie = f'cookie: {cookie_check}'
usr_ag = soup.find('div', id="user_agent").text

print(usr_ag)
print(result_cookie)
