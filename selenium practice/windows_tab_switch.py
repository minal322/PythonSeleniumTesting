import time
from calendar import prcal

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)   ### globally declared implici wait
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
#Using windowa_handles we can get all opened tabs list , index starting from o to n tabs /windows
window_obj_list = driver.window_handles

#switch to child tab
driver.switch_to.window(window_obj_list[1])

message = driver.find_element(By.TAG_NAME,"h3").text
print(message)

#switch to parent tab again
driver.switch_to.window(window_obj_list[0])

#check text on parnet window
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text