# Use BeautifulSoup package to extract “smart home” products from Amazon link

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

products = [] #creating empty list for products

table = soup.find('div', attrs= {'class': '_Y29ud_bxcGridContainer_2u9rb _Y29ud_bxcGridContainerWidth1500_36D4w _Y29ud_bxcGridmpGutterLayout_2hYHk'})
p = 0
for row in table.find_all('div', attrs={'class': '_Y29ud_bxcGridRow_Zu5i8'}):
    product = {}
    product['id'] = row[p+1].div['id']
    product['url'] = row[p+1].a['href']
    product['image'] = row[p+1].img['src']
    product['category'] = row[p+1].img['alt']
    products.append(product)

filename = 'SmartHome\BeautifulSoup_SmartHome.csv'
with open(filename, 'w', newline="") as f:
    w = csv.DictWriter(f, ['id', 'url', 'image', 'category'])
    w.writeheader
    for product in products:
        w.writerow(product)