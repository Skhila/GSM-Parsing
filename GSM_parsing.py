import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import csv

ind = 1
mobs_file = open('mobiles.csv', 'w', encoding='UTF-8_sig', newline='\n')
mobs_file_csv = csv.writer(mobs_file)
mobs_file_csv.writerow(['Model', 'Year', 'Features', 'Photo', 'Information'])
while ind <= 5:
    gsm_url = f'https://www.gsmarena.com/samsung-phones-f-9-0-p{ind}.php'
    gsm_req = requests.get(gsm_url)

    soup = BeautifulSoup(gsm_req.text, 'html.parser')
    mob_list = soup.find('div', class_='makers')
    all_mobiles = mob_list.find_all('a')

    for mobile in all_mobiles:
        mob_model = mobile.find('span').text
        if 'tablet' in mobile.img.attrs.get('title').split('.')[1].split()[-1]:
            mob_year_announced = mobile.img.attrs.get('title').split('.')[2].split()[-1]
        else:
            mob_year_announced = mobile.img.attrs.get('title').split('.')[1].split()[-1]
        mob_features = "  ".join(".".join(mobile.img.attrs.get('title').split('.')[2::]).split()[1::])
        mob_image = mobile.img.attrs.get('src')
        mob_link = mobile.attrs.get('href')
        mobs_file_csv.writerow(['Samsung ' + mob_model, mob_year_announced, mob_features, mob_image, mob_link])

    ind += 1
    sleep(randint(3, 11))
