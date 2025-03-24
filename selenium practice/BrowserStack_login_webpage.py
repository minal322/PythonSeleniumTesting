from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://bstackdemo.com/")

driver.find_element(By.ID,"signin").click()
driver.implicitly_wait(5)
#react-select-6-input

driver.find_element(By.ID,"username").click()
driver.find_element(By.CSS_SELECTOR,"value='react-select-6-input'").click()
#driver.find_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0")
driver.implicitly_wait(10)
