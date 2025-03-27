import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

#Click pn link(href) and open child window
driver.find_element(By.CLASS_NAME,"blinkingText").click()

'''
windows_handles return list of all opened windows/tabs in chrome currently.
then we can access using index starting from 0 to n 
Using driver.switch_to
'''
windows = driver.window_handles
driver.switch_to.window(windows[1])

#Extracting email from child window ,web page
email = driver.find_element(By.XPATH,"//strong/a").text
print(email)

#switching to parent tab/window
driver.switch_to.window(windows[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("password")
driver.find_element(By.ID,"terms").click()

driver.find_element(By.ID,"signInBtn").click()

wait_obj = WebDriverWait(driver,5)
wait_obj.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
message = driver.find_element(By.CSS_SELECTOR,".alert-danger").text

print(message)

time.sleep(2)



