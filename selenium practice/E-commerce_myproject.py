from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://e-commerce-minal322.vercel.app/")
driver.maximize_window()

#Inputs from user
mobile_name = "OnePlus 9 Pro"
quantity = 2

#Collect list of all mobile names
mobiles_element = driver.find_elements(By.CSS_SELECTOR,"div[class='product-card']")
print(len(mobiles_element))

# Find mobile_name in all values and click on it
for each_mob in mobiles_element:
    current_mob_name = each_mob.find_element(By.CSS_SELECTOR,"p[class='product-name']").text
    print(current_mob_name)
    if current_mob_name in mobile_name:
        each_mob.click()
        break

#Select two quantity of mobiles
driver.find_element(By.CSS_SELECTOR, "p span[class='plus']").click()

#Add to cart
driver.find_element(By.CSS_SELECTOR,".add-to-cart").click()

#Go to Cart
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()

#Pay with stripe
driver.find_element(By.XPATH,"//div/button[text()='Pay with Stripe']").click()
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div/span[.='Pay E-commerce']")))

message = driver.find_element(By.XPATH,".//div/span[.='Pay E-commerce']").text
print(message)
time.sleep(2)