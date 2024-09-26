import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
google_form="https://docs.google.com/forms/d/e/1FAIpQLSe4Zu_6Tc_ZIBKcaPVFdLWg5i52UTTcCp_xjKpzWr7bzg4-DQ/viewform?usp=sf_link"
zillio="https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zillio)
soup=BeautifulSoup(response.text,'html.parser')
address_tag=soup.find_all('address',attrs={'data-test':'property-card-addr'})
house_tag=soup.find_all('a',class_="property-card-link")
price_tag=soup.find_all('span',class_="PropertyCardWrapper__StyledPriceLine")


house_list=[]
price_list=[]
address_list=[]

for address in address_tag:
    address=str.strip(address.text)
    address_list.append(address)


for house in house_tag:
    house=house.get("href")
    house_list.append(house)



for price in price_tag:
    price=str.strip(price.text.replace("/mo",""))
    price=str.split(price,"+")
    price_list.append(price[0])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get(google_form)

for i in range(0,45):
    address_box=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_box.send_keys(address_list[i])
    time.sleep(2)

    price_box=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box.send_keys(price_list[i])
    time.sleep(2)

    house_box=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    house_box.send_keys(house_list[i])
    time.sleep(2)

    submit_button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(5)

    submit_another_response=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()
    time.sleep(5)








