from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import urllib.request
import os
from configparser import ConfigParser
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BBYbot():
	def __init__(self,config):

		self.driver = webdriver.Chrome('./chromedriver.exe')
		self.url="https://www.bestbuy.com/"
		self.username=config.get('BBY_ACCOUNT','USERNAME')
		self.password=config.get('BBY_ACCOUNT','PASSWORD')
		self.ID=config.get('BBY_ACCOUNT','ID')
		self.card=config.get('CARD_INFO','CARD#')
		self.cardsecurity=config.get('CARD_INFO','CARDSECURITY')
		self.expm=config.get('CARD_INFO','EXPM')
		self.expy=config.get('CARD_INFO','EXPY')
	

		self.driver.get(self.url)

	def Login(self):
		self.driver.find_element_by_class_name("BtnTxt").click()
		time.sleep(.5)
		self.driver.find_element_by_class_name("btn-secondary").click()
		time.sleep(2)
		username_input=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')
		username_input.send_keys(self.username)
		password_input = self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[2]/div/input')
		password_input.send_keys(self.password)
		password_input.submit()
		time.sleep(3)

		try:
			employee=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')
			employee.send_keys(self.ID)
			employee.submit()
		except:
			return

	def searchtag(self, search_tag):
		searchbar=self.driver.find_element_by_class_name('search-input')
		searchbar.send_keys(search_tag)
		searchbar.submit()

	def in_stock(self):
		time.sleep(5)
		try:
			
			item = self.driver.find_element_by_class_name('btn-lg')
			#webdriver.ActionChains(self.driver).click_and_hold(self.driver.find_elements_by_class_name('btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')).perform()
			#webdriver.ActionChains(self.driver).release().preform()
			print("In stock!")
			return True
			

		except:
			print("Item is out of stock")
			return False

	def add_toCart(self, incart):
		try:
			time.sleep(3)
			item =self.driver.find_element_by_class_name('btn-lg')
			item.click()
			time.sleep(5)							
			go_to_cart_button= self.driver.find_element_by_class_name("go-to-cart-button")
			
			go_to_cart_button.click()
			incart=True
			print("Item added to cart!")
			self.send_email_alert()
			return incart
			
		except:
			print("Couldnt add to cart trying again")
			incart=False

	def send_email_alert(self):
		sender_email = "your_email@example.com"
		receiver_email = "your_email@example.com"
		password = "your_email_password"

		message = MIMEMultipart("alternative")
		message["Subject"] = "Item Added to Cart"
		message["From"] = sender_email
		message["To"] = receiver_email

		text = """\
		Hi,
		The item has been added to your cart. Please complete the checkout process."""
		part = MIMEText(text, "plain")
		message.attach(part)

		with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
			server.login(sender_email, password)
			server.sendmail(
				sender_email, receiver_email, message.as_string()
			)

	def closeEmailprompt(self):
		self.driver.find_element_by_class_name("c-modal-close-icon").click()
	def close(self):
		self.driver.close()
def getinput():
	sku_num=skunumber.get()
	print(sku_num)
	return sku_num

print("Starting Bot")
searchtag=''
config_file= ConfigParser()
config_file.read("config.ini")
bot = BBYbot(config_file)
time.sleep(1)
try:
	bot.Login()
except:
	bot.closeEmailprompt()
	time.sleep(3)
	bot.Login()
time.sleep(4)
bot.searchtag("6614262")
instock= bot.in_stock()
incart=False
if (instock==True):
	while(incart != True):
	 	incart=bot.add_toCart(incart)
print("In cart!")
time.sleep(1)

print("compiled")
bot.close()
