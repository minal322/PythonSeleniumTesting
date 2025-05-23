import os.path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


driver = webdriver.Chrome()
''''' Scroll to element and click '''
# driver.get("https://demoblaze.com/index.html")
# driver.implicitly_wait(5)
# action = ActionChains(driver)
# element = driver.find_element(By.LINK_TEXT,"Sony vaio i7")
# #scroll to element and click
# action.scroll_to_element(element).perform()
# element.click()


'''   '''
# driver.get("https://demoblaze.com/index.html")
# driver.implicitly_wait(5)
#
# driver.find_element(By.ID,"signin2").click()
# driver.find_element(By.ID,"sign-username").send_keys("Minal")
# time.sleep(5)

''' Switch to tab/window using window_handles'''
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.implicitly_wait(5)
# driver.find_element(By.LINK_TEXT,"Click Here").click()
# window_obj_list = driver.window_handles
# driver.switch_to.new_window(window_obj_list[1])
# print(driver.title)
# text = driver.find_element(By.TAG_NAME,"h3").text
# print(text)

''' Upload file using send_keys(filepath)'''
# driver.get("https://the-internet.herokuapp.com/upload")
# driver.implicitly_wait(5)
# element = driver.find_element(By.ID,"file-upload")
# element.send_keys("C:/Users/Admin/Downloads/abc.txt")
# # element.click()
# driver.find_element(By.ID,"file-submit").click()

'''Context click right click and switch to alert'''
# driver.get("http://the-internet.herokuapp.com/context_menu")
# driver.implicitly_wait(5)
# element = driver.find_element(By.ID,"hot-spot")
# action = ActionChains(driver)
# action.context_click(element).perform()
# text = driver.switch_to.alert.text
# driver.switch_to.alert.accept()
# print(text)


driver.get("http://the-internet.herokuapp.com/context_menu")
driver.implicitly_wait(5)

time.sleep(5)
driver.quit()