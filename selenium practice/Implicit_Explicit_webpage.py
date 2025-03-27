import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)   ### globally declared implici wait
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Vegitable shopping using implicity and explicit waits
'''
Implicit wait is like global timeout . If any element is not shown on web page then it waits for the element to bfound.
If element is displayed in 2 seconds then it moves ahed insted of waitng for specific time

'''
#search ber value
driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
time.sleep(2)
#Store all elements displayed on webpage after entering value in search box
veg_results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# time.sleep(2)
print(len(veg_results))
assert len(veg_results) > 0

for each_veg in veg_results:
    each_veg.find_element(By.XPATH, "div/button").click()

###Assignment - Expected list of items name should be equal to actual list
expected_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
product_names = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
actual_list = []
for each_name in product_names:
    name = each_name.text
    actual_list.append(name)
print(actual_list)
print(expected_list)
assert actual_list == expected_list

#click on go to cart icon
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

#click on proceed to checkout
driver.find_element(By.CLASS_NAME,"action-block").click()
# time.sleep(3)


#Validation for Acutal price to total price
#get all values from table
veg_prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(total_amount)
calculated_price = 0
for each_veg in veg_prices:
    price = int(each_veg.text)
    calculated_price = price + calculated_price

print(calculated_price)
assert calculated_price == total_amount


#add promo code
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
#click apply button
driver.find_element(By.CSS_SELECTOR,"div button[class='promoBtn']").click()
# driver.implicitly_wait(5)
#Fetch promo code applied message
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promo_message = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

### Assignment - Total after discount should always less than total amount

total_after_discount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
assert int(float(total_after_discount)) < total_amount
#print(total_after_discount)


time.sleep(2)