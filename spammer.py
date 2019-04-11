from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import sys
import requests

driver = webdriver.Chrome('./chromedriver')

wait = WebDriverWait(driver, 600)

driver.get("https://web.whatsapp.com/")

# ActionChains = ActionChains(driver)
# driver.get("https://source.unsplash.com/random")
# images = driver.find_element_by_tag_name('img')
# ActionChains.move_by_offset(254, -322).perform()

# time.sleep(2)

# print(images)

target = '"Amit"'

x_arg = '//span[contains(@title,' + target + ')]'
target_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
target_title.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

for i in range(1, 150):
	message.send_keys(i)
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()
