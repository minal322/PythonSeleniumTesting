from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service_obj = Service("C:/Users/Admin/Downloads/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.get("https://www.browserstack.com/selenium")
print(driver.title)
print(driver.current_url)
print(driver.name)
time.sleep(2)