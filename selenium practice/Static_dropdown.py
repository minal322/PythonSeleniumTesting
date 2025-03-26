#https://rahulshettyacademy.com/angularpractice/
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# create service for giving path of Service class
service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# create webdriver object with providing service
driver = webdriver.Chrome(service=service_obj)

# Open browser for any url/application you want to test
driver.get("https://rahulshettyacademy.com/angularpractice/")


""" To Select value from SELECT tag we need to use Select class
import Select class
Create object of Select class 
use in built methods of select class

"""
# Find Gender element and enter value in web page
#driver.find_element(By.ID,"exampleFormControlSelect1").send_keys("Female")
#OR
gender_object = Select(driver.find_element(By.ID ,"exampleFormControlSelect1" ))
gender_object.select_by_visible_text("Female")

'''
OR 
gender_object.select_by_index(2)   ==== give index starting from 0
OR
gender_object.select_by_value("Female") ==== give value="Female", if value attribute is present
'''