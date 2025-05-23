#frame1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/key_presses")
# driver.implicitly_wait(5)
#
#
# mouse = ActionChains(driver)
# key = 'j'
# textbox = driver.find_element(By.ID,"target")
# mouse.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL,
# perform()
# text = driver.find_element(By.ID,"result").text
# print(text)
# print(text)
#
# driver.quit()


driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")

action = ActionChains(driver)

element = driver.find_element(By.XPATH,"//legend[text()='iFrame Example']")
action.scroll_to_element(element).perform()

time.sleep(10)
