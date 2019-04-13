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


#### All the Modes functions:

# image spammer function
def images_spammer():
	print("Ok, so images spaming! let's get started!\n")

	image_subject = "random"


	# image random ask
	if strtobool(raw_input("\n\n	Would You like a random images? [Yes/No] : ")):
		print "	Okay, I will spam", target ,"with",image_subject,"images"
	else:
		image_subject = raw_input("	Okay, what is the subject of your images?: ").lower()
		image_subject = "1600x900/?" + image_subject

	for i in range(min, max + 1):
		# open unsplash
		driver.get("https://source.unsplash.com/"+ image_subject)

		if driver.current_url == "https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200":
			print("Please enter a real subject")
			exit()
			driver.close()

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
		time.sleep(4.5)

		if i == max+1:
			print("Thank you! I finish here.")

# text spammer function
def text_spammer(max):
	max = max
	print("Alright, so text spaming! let's get started!")
	massage = raw_input("\n\n	What is your massage?: ")
	max = input("\n	because it's text spamming you may want to send more, so you can change the num of massages now: ")
	print("max is: " + str(max))

	# open whatsapp
	driver.get("https://web.whatsapp.com/")

	# delay
	time.sleep(4)

	# find target
	x_arg = '//span[contains(@title,"' + target + '")]'
	group_title = wait.until(EC.presence_of_element_located((
		By.XPATH, x_arg)))
	group_title.click()

	for i in range(min, max + 1):
		# enter i into massage
		message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
		message.send_keys(massage,i)

		# send massage
		sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
		sendbutton.click()

		if i == max+1:
			print("Thank you! I finish here.")

# sticker spammer function
def sticker_spammer():
	print("So sticker spaming! let's get started!\n")


print("\n\nWelcome to the whatsapp web image spammer! \nplease answer the next questions:\n")

# vars
image_subject = "random"
min = 0
max = input("	please enter how much would you like to spam your frind? \n	** don't make a large number it will take a lot of time and it can make bugs!\n 	so please:")
if max <= 0:
	print("			You have to enter a number that is bigger then 0, try again later")
	exit()
	driver.close()

# target
target = raw_input("	Who is the target?: ")
if len(target) < 0:
	print("			! You have to enter a target, try again later")
	exit()
	driver.close()

# mode
mode = raw_input("	Please choose mode:\n		(a) image spaming [type a]\n		(b) text spaming [type b]\n		I choose: ")

# drivers
keyboard = Controller()
driver = webdriver.Chrome('./chromedriver')

# wait
wait = WebDriverWait(driver, 600)

# mode chooser
if mode == "a":
	images_spammer()
elif mode == "b":
	text_spammer(max)
else :
	print("	! please next time enter a real mode")
	exit()
	driver.close()
