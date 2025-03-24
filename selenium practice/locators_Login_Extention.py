
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# create service for giving path of Service class
service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# create webdriver object with providing service
driver = webdriver.Chrome(service=service_obj)

# Open browser for any url/application you want to test
driver.get("https://rahulshettyacademy.com/client")


driver.find_element(By.LINK_TEXT,"Forgot password?").click()

''' XPATH  
we can find xpath from parent tag to child path eg: //form/div//input
If there are multiple child tags then you can use square brackets with index (1 to n)
//form/div[1]/input or //form/div[2]/input
'''
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

''' CSS_SELECTOR - In css we use space insted of slash for traversing to the element.
we can find css selector path from parent tag to child path eg: form div input
If there are multiple child tags then we can find child using :nth-child(n)
Eg : form div:nth-child(2) input
'''
driver.find_element(By.CSS_SELECTOR , " form div:nth-child(2) input").send_keys("Hello@1234")

driver.find_element(By.CSS_SELECTOR , " form div:nth-child(3) input").send_keys("Hello@1234")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(5)