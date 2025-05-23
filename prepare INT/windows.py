from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.implicitly_wait(5)
title = driver.title
# element = driver.find_element(By.ID,"tabButton")
# driver.execute_script("arguments[0].scrollIntoView();",element)
# print(driver.title)
# element.click()

# print(len(current))
# driver.switch_to.new_window(current[1])
current_window = driver.current_window_handle

ele2 = driver.find_element(By.ID,"messageWindowButton")
driver.execute_script("arguments[0].scrollIntoView();",ele2)
ele2.click()
wait = WebDriverWait(driver,10)
wait.until(ec.number_of_windows_to_be(2))


print(len(driver.window_handles))
for win in driver.window_handles:
    if(win != current_window):
     driver.switch_to.window(win)

print(driver.title)
driver.switch_to.default_content()
time.sleep(5)
driver.quit()
# driver.find_element(By.ID,"messageWindowButton").click()
# driver.switch_to.
