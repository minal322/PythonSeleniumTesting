'''
https://rahulshettyacademy.com/seleniumPractise/#/
To select true
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

search_vegs = driver.find_element(By.XPATH , "//form/input")
search_vegs.send_keys("Brocolli")
driver.implicitly_wait(2)

total_veg_count = 5
i = 1

while(i <= total_veg_count):
    driver.find_element(By.XPATH, "//a[@class='increment']").click()
    driver.implicitly_wait(2)
    i= i+1

driver.find_element(By.XPATH , "//div/button[.='ADD TO CART']").click()

driver.find_element(By.XPATH , "//div/a[4]").click()

driver.find_element(By.XPATH , "//div/button[.='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(2)

driver.find_element(By.XPATH, "//div/button[.='Place Order']").click()
driver.implicitly_wait(2)

'''
SELECT code missing
//div/select/option[.='India']
'''
driver.find_element(By.XPATH, "//div/select/option[.='India']").click()
driver.implicitly_wait(2)

driver.find_element(By.CLASS_NAME,"chkAgree").click()
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//div/button[.='Proceed']").click()

'''
To Check if order placed successfully we will fetch text from webpage and add assertion to it
'''
driver.implicitly_wait(5)
message = driver.find_element(By.XPATH,"//div[@class='wrapperThree']").get_attribute("value")

print(message)

time.sleep(5)