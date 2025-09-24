# Use Selenium method to extract “smart home” products from above Amazon link

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = 'https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2'

cService = webdriver.ChromeService(executable_path='C:\\Users\\testi\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(url)

CategoriesList=[]
CategoriesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, '_Y29ud_bxcGridRow_Zu5i8')]")

for c in range(len(CategoriesDiv)-1):
            Categories = {}
            innerImg = CategoriesDiv[c+1].find_element(By.TAG_NAME, "img")
            Categories["Category"] =innerImg.get_attribute('alt') 
            CategoriesList.append(Categories)

for p in CategoriesList:
     

