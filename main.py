import json
import requests
from bs4 import BeautifulSoup as bs

users = ['had.eelflower', 'amro__2023', 'emanista_academy','reemalaadesign', 'saharsyoussef', 'reemalaadesign']

for i in users:
    r = requests.get(f'http://instagram.com/{i}')
    soup = bs(r.text, 'html.parser')
    general_data = soup.find_all('meta', attrs={'property': 'og:description'})
    description = soup.find('script', attrs={'type': 'application/ld+json'})
    description = json.loads(description.get_text())
    text = general_data[0].get('content').split()
    Followers = str(text[0]).strip().replace('\n', '')
    print(f'{i} ===> {Followers}')
