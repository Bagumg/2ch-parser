import requests
from bs4 import BeautifulSoup
import wget
import re

r = requests.get('https://2ch.hk/e/res/435298.html')

soup = BeautifulSoup(r.text, 'lxml')

for i in soup.find_all('a', class_='post__image-link'):
    # print(re.search(r'/[0-9]{7,}.\D[0-9]*\D[0-9]*\D[0-9]*', i['href']))
    s = re.search(r'[0-9]{7,}.\D[0-9]*\D[0-9]*\D[0-9]*', i['href'])
    # print(s.group(0))
    z = 1
    wget.download(f'https://2ch.hk{i["href"]}', s.group(0))

