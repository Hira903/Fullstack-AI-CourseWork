# Use BeautifulSoup package to extract “smart Phone” products from above Daraz link
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")

products = []
table = soup.find("div", attrs={'data-qa-locator':'general-products'})

for row in table.find_all("div", attrs={'class':'Bm3ON'}):
    product = {}
    product['Product_ID'] = row.div["data-item-id"]
    product['URL'] = row.a["href"]
    product['Specs'] = row.img["alt"].split('-', )