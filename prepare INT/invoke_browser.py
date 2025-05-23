import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# # # #another way is maually load driverv
# # # #C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe
# # service_obj = Service("C:/Users/Admin/Download/edgedriver_win64/msedgedriver.exe")
# # driver = webdriver.Edge(service=service_obj)
# # driver.get("https://rahulshettyacademy.com/angularpractice/")
# # time.sleep(5)
#
#
# service_obj = Service("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
# driver = webdriver.Edge(service=service_obj)
# driver.get("https://www.browserstack.com/selenium")
# print(driver.title)
# print(driver.current_url)
# print(driver.name)
# time.sleep(2)


driver.get_screenshot_as_file("demo2.png")
driver.get_screenshot_as_png()