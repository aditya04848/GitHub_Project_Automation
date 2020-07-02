import os
from selenium import webdriver
import time

what = input("Do you want to make a new folder?(y/n):    ")
directory = input("Enter the repositore/project name:    ",)
repo = input("Do you have a GitHub Repository?(y/n):    ")
commitq = input("Do you want to commit the changes? (y/n):    ")
if(commitq == 'y'):
        message = input("Enter the message for commit:    ")

parent_dir = "E:/Projects/"
path = os.path.join(parent_dir, directory) 
if(what == 'y'):
        os.mkdir(path) 
        print("Directory '% s' created" % directory) 

username = 'AtulSingh72'
password = 'mybdayon0204'

class Carry():
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='E:/Web Automation/chromedriver.exe')

	def play(self, name):
                print("Just sit back and relax........We will create the repository for you.")
                self.driver.get('https://github.com/login')
                search = self.driver.find_element_by_xpath('//*[@id="login_field"]')
                search.send_keys(username)
                search = self.driver.find_element_by_xpath('//*[@id="password"]')
                search.send_keys(password)
                searchon = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
                searchon.click()
                self.driver.get('https://github.com/new')
                search = self.driver.find_element_by_xpath('//*[@id="repository_name"]')
                search.send_keys(directory)
                time.sleep(4)
                search = self.driver.find_element_by_css_selector('button.first-in-line')
                search.click()

if(repo == 'n'):
        bot = Carry()
        bot.play(directory)

URL = "https://github.com/"+username+"/"+directory+".git"

import subprocess as cmd

if(commitq == 'y'):
        os.system("cd "+path+" && git init && git add . && git commit -m "+message+" && git remote add origin "+URL+" && git push -f origin master")
else:
        os.system("cd "+path+" && git init && git add .")
