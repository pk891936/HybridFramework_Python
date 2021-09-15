import pytest,logging
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage_Actions import AddCustomer
from utilities.readProperties import readConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import string
import random


baseURL = "https://admin-demo.nopcommerce.com"
username = "admin@yourstore.com"
password = "admin"
 # Logger


print("************* Test_Tabledata_Extraction **********")

driver = webdriver.Chrome(executable_path="C://Users//Praveen//PycharmProjects//Hybrid_Framework//Drivers//chromedriver.exe")
driver.get(baseURL)
lp = LoginPage(driver)
print("************input Username*************")
driver.find_element_by_id(lp.textbox_username_id).clear()
driver.find_element_by_id(lp.textbox_username_id).send_keys(username)
print("************input Password*************")
driver.find_element_by_id(lp.textbox_password_id).clear()
driver.find_element_by_id(lp.textbox_password_id).send_keys(password)
print("************clicking Login*************")
driver.find_element(By.XPATH, lp.button_login_xpath).click()
print("************Login Successfull*************")
#driver.implicitly_wait(3)
print("******* Starting Add Customer Test **********")
addcust = AddCustomer(driver)
wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,
                      ElementNotVisibleException,ElementNotSelectableException])
#wait.until(EC.invisibility_of_element_located((By.XPATH, "//input[@id='message']")))
wait.until(EC.presence_of_element_located((By.XPATH,addcust.lnkCustomers_menuitem_xpath)))
driver.find_element(By.XPATH ,addcust.lnkCustomers_menu_xpath).click()
driver.find_element(By.XPATH, addcust.lnkCustomers_menuitem_xpath).click()
driver.implicitly_wait(3)
print("************* Extracting customer info **********")
rows = 1+ len(driver.find_elements(By.XPATH,"//*[@id='customers-grid']/tbody/tr"))
cols = 1 + len(driver.find_elements(By.XPATH, "//*[@id='customers-grid']/tbody/tr[1]/td"))
print("rows = ",rows, "columns =",cols)
for i in range(1,rows):
    for p in range(2,cols):
        value = driver.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(i)+"]/td["+str(p)+"]").text
        print(value, end="      ")
    print()
driver.quit()
print("******* Extracted data fromtable successfully **********")

