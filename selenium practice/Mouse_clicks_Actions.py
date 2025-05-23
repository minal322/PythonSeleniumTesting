
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)   ### globally declared implici wait
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

'''
Mouse Actions Demo

'''
action = ActionChains(driver)

#hover to button
action.move_to_element(driver.find_element(By.ID,"mousehover")).click().perform()

#right click on top
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
