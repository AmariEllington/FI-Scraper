from selenium import webdriver
import csv

chrome_path = r'/Applications/chromedriver'

driver = webdriver.Chrome(chrome_path)
driver.get('https://www.footballindex.co.uk/top-200')
names = driver.find_elements_by_class_name("""Pic__container__name___26P8X""")


with open('football.index.csv', 'w', newline='') as csvfile:
    field_names = ['name', 'buy', 'sell']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

for i in range(0, len(names)):
    playerName = driver.find_elements_by_class_name(
        """Pic__container__name___26P8X""")[i].text

    buyingPrice = driver.find_elements_by_id("""buy""")[i].text

    sellingPrice = driver.find_elements_by_id("sell")[i].text

driver.quit()
