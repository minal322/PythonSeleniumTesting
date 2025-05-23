#frame1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.implicitly_wait(5)

current_window = driver.current_window_handle


