from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")

message = input("Enter your message: ")
num = int(input("Enter number of times: "))

input("\nPress enter to begin")

inputText =  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(num):
    inputText.send_keys(message)
    inputText.send_keys(Keys.ENTER)
