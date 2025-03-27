from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")
'''
For clicking on courses link

driver.find_element(By.CSS_SELECTOR,"a[href='https://courses.rahulshettyacademy.com/courses']").click()

driver.switch_to.default_content()
windows_list = driver.window_handles
driver.switch_to.window(windows_list[1])

driver.find_element(By.ID,"search-courses").send_keys("Testing")
driver.find_element(By.ID,"search-course-button").click()

driver.switch_to.window(windows_list[0]) 
'''

'''
For Clicking on iframe blog page  ---> Click Here Button ----> new tab open
'''
