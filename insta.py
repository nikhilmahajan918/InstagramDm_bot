#importing required python packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import random

#function InstaDm that sends the dm to any user
def InstaDm(username,password,person,dm):
	#chrome driver stored location 
	driver = webdriver.Chrome('/home/nikhil/Desktop/Instagram_bot/chromedriver')
	#accessing instagram url 
	driver.get("https://www.instagram.com/")
	#entering username in instagram website that has been passed as parameter of function InstaDm
	enter_username = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'username')))
	enter_username.send_keys(username)

    #entering password in instagram website that has been passed as parameter of function InstaDm
	enter_password = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
	enter_password.send_keys(password)
	enter_password.send_keys(Keys.RETURN)
	time.sleep(random.randint(1,4))

    #if after login, the instagtam prompts for save password,
    # this block of code hit enter the not now button
	try:
		not_now = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
		a= not_now.find_elements_by_tag_name("button")[1]
		actions = ActionChains(driver)
		actions.click(a)
		actions.perform()
	#if there is no prompt of save password, 
	#it passes the condition and sends the dm directly to the user 	
	except:
		pass
	#this piece of code click the inbox button
	finally:
		inbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'xWeGp')))
		actions = ActionChains(driver)
		actions.click(inbox)
		actions.perform()
		time.sleep(random.randint(1,4))
    #this is for clicking the not now option for sending notification prompt 
	try:
		not_now = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
		a= not_now.find_elements_by_tag_name("button")[1]
		actions = ActionChains(driver)
		actions.click(a)
		actions.perform()
	#if there is no prompt of send notifications, it will pass the condition
	except:
		pass
	finally:
		new_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'QBdPU')))
		actions = ActionChains(driver)
		actions.click(new_message)
		actions.perform()

	enter_person_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'queryBox')))
	enter_person_name.send_keys(person)

	time.sleep(random.randint(1,4))

	select_person = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'dCJp8')))
	actions1 = ActionChains(driver)
	actions1.click(select_person)
	actions1.perform()

	next_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'rIacr')))
	actions1 = ActionChains(driver)
	actions1.click(next_button)
	actions1.perform()

	messagebox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
	messagebox.send_keys(dm)
	time.sleep(random.randint(1,3))
	messagebox.send_keys(Keys.RETURN)

InstaDm("itscoder8295","1234boitesting","virat.kohli","hello sir")






