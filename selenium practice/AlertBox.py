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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Minal Patil"
#Send name into textbox
driver.find_element(By.ID,"name").send_keys(name)
#Click on alert button
driver.find_element(By.ID,"alertbtn").click()
"""
selenium webdriver cannot directly accesss alert , thats why we need to switch to alert obj
"""
alert = driver.switch_to.alert

#Used to retrive message in alert box
message = alert.text
#assertion to check of name is present in alert or not
assert name in message

#method in alert to click ok,confirm,accept,yes
alert.accept()

time.sleep(5)


