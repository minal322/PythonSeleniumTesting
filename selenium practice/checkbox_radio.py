from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# create service for giving path of Service class
service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# create webdriver object with providing service
driver = webdriver.Chrome(service=service_obj)

# Open browser for any url/application you want to test
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

""" Checkbox whose if alginment changes than we can use for loop to find checkbox value and select
    For that we will use findElements() method which returns list of all checkboxes
"""

checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxes:
    if(checkbox.get_attribute("value") == "option2"):
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,'input[type="radio"]')
for radio in radiobuttons:
    if(radio.get_attribute("value") == "radio3"):
        radio.click()
        assert radio.is_selected()
        break
#OR
# If we know fixed location of radio option , can use index
#radiobuttons[3].click()
#radiobuttons[3].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
print("Textbox is default displayed")

driver.find_element(By.ID,"hide-textbox").click()
print("Clicked on Hide button to hide textbox ")
assert driver.find_element(By.ID,"displayed-text").is_displayed()
