#https://rahulshettyacademy.com/angularpractice/
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# create service for giving path of Service class
service_obj = Service("C:/Users/Admin/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# create webdriver object with providing service
driver = webdriver.Chrome(service=service_obj)

# Open browser for any url/application you want to test
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Now Enter email,password and check checkbox using selenium
#to do that we have locators in selenium
"""
    First explore web page and inspect to know elements name,unique id etc
        Name : name=name
        Email : name=email
        password : ID = exampleInputPassword1
        checkbox : ID = exampleCheck1
        Gender : ID = exampleFormControlSelect1
        Employment Status : ID = inlineRadio2
        DOB : name = bday (mm/dd/yyyy)
"""
# Find name element using find_element() by its id or name.
# And send input using send_keys() by entering key(Minal Patil) in web page

""" Name Field USING CSS_SELECTOR --- 
Gender : nane = name, tagname = input ,
CSS_SELECTOR Syntax : tagname[attribute = value]  Eg: input[@name = "name"] or #id +or .classname
"""
#driver.find_element(By.NAME, "name").send_keys("Minal Patil")
driver.find_element(By.CSS_SELECTOR, "input[@name = 'name'] ").send_keys("Minal Patil")

# Find email element by its id or name and enter value in web page
driver.find_element(By.NAME , "email").send_keys("patilminu322@gmail.com")

# Find Password element and enter value in web page
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123minu")

# Find Checkbox element and click checkbox in web page
driver.find_element(By.ID,"exampleCheck1").click()

# Find Gender element and enter value in web page
driver.find_element(By.ID,"exampleFormControlSelect1").send_keys("Female")

#Find Radio button element and enter click in web page
driver.find_element(By.ID,"inlineRadio2").click()
#using css
#driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

# Find Date of Birth element and enter value in web page
driver.find_element(By.NAME,"bday").send_keys("06/25/2001")

""" SUBMIT BUTTON USING XPATH
submit : class = btn btn-success , type = submit , value = submit
XPATH Syntax :-  //tagname[@attribute=value]  Eg: //input[@type="submit"] or //input[@value=submit]
"""
driver.find_element(By.XPATH,"//input[@type='submit']").click()

'''When form is submitted alert/message is displayed. To get/extract message form web page use text
 Success message : class = alert alert-success alert-dismissible (use one class from these three classes)
'''
#browser text is stored in message variable
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

driver.find_element_by_name()
#To validate login is success
assert "Success" in message

time.sleep(10)


