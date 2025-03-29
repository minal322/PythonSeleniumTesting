from pydoc import browse

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(3)
driver.maximize_window()

sorted_list = []
browser_list = []
#click on table colum 1st
driver.find_element(By.XPATH,"//span[.='Veg/fruit name']").click()

#collecting tables veggies list after clicking(browser sorted list)

veggies_list= driver.find_elements(By.XPATH, "//tr/td[1]")

for each_veg in veggies_list:
    veg_name = each_veg.text
    sorted_list.append(veg_name)
    browser_list.append(veg_name)

#sorting sorted list now
sorted_list.sort()

#Validating both list are same
assert sorted_list == browser_list

