from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from distutils.util import strtobool
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform
import os, sys


#### All the Modes functions:

# image spammer function
def images_spammer():
	# welcome to the function
	print("\nOk, so images spaming! let's get started!\n")

	# get max
	max = input("	please enter how much would you like to spam your frind? \n	** don't make a large number it will take a lot of time and it can make bugs!\n 	so please:")

	# check max
	if max <= 0:
		print("			You have to enter a number that is bigger then 0, try again later")
		exit()
		driver.close()

	# print max
	print("max is: " + str(max))


	# image defult subject
	image_subject = "random"

	# image random ask
	if strtobool(raw_input("\n\n	Would You like a random images? [Yes/No] : ")):
		print "	Okay, I will spam", target ,"with",image_subject,"images"
	else:
		image_subject = raw_input("	Okay, what is the subject of your images?: ").lower()
		image_subject = "1600x900/?" + image_subject

	print("Okay now scan the qr code on the whatsapp web and let the magic begin.")

	for i in range(min, max):
		# open unsplash
		driver.get("https://source.unsplash.com/"+ image_subject)

		if driver.current_url == "https://images.unsplash.com/source-404?fit=crop&fm=jpg&h=800&q=60&w=1200":
			print("Please enter a real subject")
			exit()
			driver.close()

		# copy img
		keyboard.press(system_control)
		keyboard.press('c')
		keyboard.release('c')
		keyboard.release(system_control)

		# delay
		time.sleep(1)

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
		keyboard.press(system_control)
		keyboard.press('v')
		keyboard.release('v')
		keyboard.release(system_control)

		# delay
		time.sleep(1)

		# send img
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		# delay
		time.sleep(5)

		if i == max+1:
			print("Thank you! I finish here.")

# text spammer function
def text_spammer(max):
	# welcome to the function
	print("\nAlright, so text spaming! let's get started!")

	# get max
	max = input("	please enter how much would you like to spam your frind?:")

	# check max
	if max <= 0:
		print("			You have to enter a number that is bigger then 0, try again later")
		exit()
		driver.close()

	print("Okay now scan the qr code on the whatsapp web and let the magic begin.")

	massage = raw_input("\n\n	What is your massage?: ")
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

	for i in range(min, max):
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
	print("\nSo sticker spaming! let's get started!\n")

	# get max
	max = input("	please enter how much would you like to spam your frind?:")

	# check max
	if max <= 0:
		print("			You have to enter a number that is bigger then 0, try again later")
		exit()
		driver.close()

	print("Okay now scan the qr code on the whatsapp web and let the magic begin.")

	# open whatsapp
	driver.get("https://web.whatsapp.com/")

	# delay
	time.sleep(4)

	# find target
	x_arg = '//span[contains(@title,"' + target + '")]'
	group_title = wait.until(EC.presence_of_element_located((
		By.XPATH, x_arg)))
	group_title.click()

	# delay
	time.sleep(1)

	# emoji_button click
	emoji_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div/div[2]/button')
	emoji_button.click()

	# delay
	time.sleep(1)

	# sticker_button
	sticker_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div/div[4]/button')
	sticker_button.click()

	time.sleep(2)


	for i in range(min,max):
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div/img').click()

print("\n\nWelcome to the whatsapp web image spammer! \nplease answer the next questions:\n")

# vars
image_subject = "random"
min = 0
system_control = "ctrl"

# check platform
if platform.system() == "Darwin":
	system_control = Key.cmd
elif platform.system() == "Windows":
	system_control = Key.ctrl
elif platform.system() == "Linux":
	print("Sorry I can't help for Linux")
	exit()

# target
target = raw_input("	Who is the target?: ")
if len(target) < 0:
	print("			! You have to enter a target, try again later")
	exit()
	driver.close()

# mode
mode = raw_input("	Please choose mode:\n		(a) image spaming [type a]\n		(b) text spaming [type b]\n		(c) sticker spaming [type c]\n		I choose: ")

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
elif mode == "c":
	sticker_spammer()
else :
	print("	! please next time enter a real mode")
	exit()
	driver.close()
