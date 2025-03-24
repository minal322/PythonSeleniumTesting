import time
from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time

#driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver.get("https://www.browserstack.com/selenium")
print(driver.current_url)
print(driver.title)
time.sleep(2)

