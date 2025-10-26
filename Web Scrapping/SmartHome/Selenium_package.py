# Use Selenium method to extract “smart home” products from above Amazon link

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = 'https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2'

cService = webdriver.ChromeService(executable_path='C:\\Users\\testi\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(url)
driver.maximize_window()

searchBox = driver.find_element(By.ID, "twotabsearchtextbox")
searchBox.clear()
searchBox.send_keys("Smart Home Products")

Searchbutton = driver.find_element(By.ID, "nav-search-submit-button")
Searchbutton.click()

driver.find_element(By.XPATH, "//span[text()='Amazon.com']").click()

Categories_List = []
Nmaes_List = []
Prices_List = []
Ratings_List = []

# all items
# all names
driver.find_elements(By.XPATH, ""
# prices
# Ratings
# Categories

driver.close()