from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(3)

mobile = "Samsung Note 8"

# can also done by using CSS_SELECTOR "a[href*='shop']" (regular expression *=)
driver.find_element(By.XPATH,"//a[text()='Shop']").click()

#Store web-elements of all product in a list ---
app_cards = driver.find_elements(By.XPATH,"//div/app-card-list/app-card")
print(len(app_cards))
for each_card in app_cards:
    m_text = each_card.find_element(By.CSS_SELECTOR,"div h4 a").text
    if m_text == mobile:
        #Add product to the cart
        each_card.find_element(By.CSS_SELECTOR,".btn-info").click()
        break

#checkout
driver.find_element(By.CSS_SELECTOR,".btn-primary").click()

#payment
driver.find_element(By.CSS_SELECTOR,".btn-success").click()

###Explicit Wait
#dynamic input dropdown
#send India
driver.find_element(By.CSS_SELECTOR,".filter-input").send_keys("India")
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='suggestions'] ul li")))
driver.find_element(By.CSS_SELECTOR,"div[class='suggestions'] ul li").click()

'''
OR
#send ind
driver.find_element(By.CSS_SELECTOR,".filter-input").send_keys("ind")
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
'''

#click checkbox
driver.find_element(By.CSS_SELECTOR,"div label[for='checkbox2']").click()

#purchase
driver.find_element(By.CSS_SELECTOR,".btn-success").click()

#fetch message and verify
message = driver.find_element(By.CSS_SELECTOR,".alert-success").text
print(message)
assert "Success" in message

driver.close()