import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[contains(@class,'l ng-pristine ng-invalid ng-touched')]").send_keys("minal")
# print("wait")
# # driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

select_obj = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
select_obj.select_by_visible_text("Female")
time.sleep(5)
