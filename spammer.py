from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os, sys
import requests
from pynput.keyboard import Key, Controller
from distutils.util import strtobool


#### All the functions:

# image spammer function
def images_spammer():

	# image random ask
	if strtobool(raw_input("	Would You like a random images? [Yes/No] : ")):
		print "	Okay, I will spam", target ,"with random images"
	else:
		image_subject = raw_input("	Okay, what is the subject of your images?: ").lower()
		image_subject = "1600x900/?" + image_subject

	# some text
	print("\nimage_subject is: " + image_subject)

	for i in range(min, max + 1):
		# open unsplash
		driver.get("https://source.unsplash.com/"+ image_subject)

		if driver.current_url == "https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200":
			print("Please enter a real subject")
			exit()

		# copy img
		keyboard.press(Key.cmd)
		keyboard.press('c')
		keyboard.release('c')
		keyboard.release(Key.cmd)

		# open whatsapp
		driver.get("https://web.whatsapp.com/")

		# delay
		time.sleep(4)

		# find target
		x_arg = '//span[contains(@title,"' + target + '")]'
		print("x_arg is :", x_arg)
		group_title = wait.until(EC.presence_of_element_located((
			By.XPATH, x_arg)))
		group_title.click()

		# paste img
		keyboard.press(Key.cmd)
		keyboard.press('v')
		keyboard.release('v')
		keyboard.release(Key.cmd)

		# delay
		time.sleep(1)

		# send img
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		# delay
		time.sleep(5)

		# enter i into massage
		message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
		message.send_keys("this is image number ",str(i)," from ",str(max)," images")

		# send i
		sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
		sendbutton.click()

		# delay
		time.sleep(4.5)


print("Welcome to the whatsapp web image spammer! \nplease answer the next questions:\n")

# vars
image_subject = "random"
min = 0
max = input("	please enter how much would you like to spam your frind?: ")
if max <= 0:
	print("			You have to enter a number that is bigger then 0, try again later")
	exit()

# target
target = raw_input("	Who is the target?: ")
if len(target) < 0:
	print("			You have to enter a target, try again later")
	exit()

# mode
mode = raw_input("Please choose mode:\n		(a)image spaming[type a]\n		(b) text spaming[type b]\n		(c) sticker spaming[type c]\n")

# drivers
keyboard = Controller()
driver = webdriver.Chrome('./chromedriver')

# wait
wait = WebDriverWait(driver, 600)

# mode chooser
if mode == "a":
	images_spammer()
elif mode == "b":
	text_spammer()
elif mode == "c":
	sticker_spammer()
else :
	print("please next time enter a real mode")
	driver.close()
	exit()
