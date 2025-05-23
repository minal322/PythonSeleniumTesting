from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.implicitly_wait(5)

#driver.find_element(By.XPATH,"//div[@class='row']/div/button[contains(@class,'btn btn-primary')]").click()
element = driver.find_element(By.XPATH,"//button[@id='alertButton'] ")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
text = driver.switch_to.alert.text
driver.switch_to.alert.accept()
print(text)

driver.find_element(By.XPATH,"//button[@id='timerAlertButton']").click()
wait = WebDriverWait(driver,10)
wait.until(ec.alert_is_present())
text = driver.switch_to.alert.text
driver.switch_to.alert.accept()
print(text)

driver.find_element(By.ID,"confirmButton").click()
text = driver.switch_to.alert.text
driver.switch_to.alert.dismiss()
print(text)

driver.find_element(By.ID,"promtButton").click()
driver.switch_to.alert.send_keys("Minal Patil Great")
driver.switch_to.alert.accept()

