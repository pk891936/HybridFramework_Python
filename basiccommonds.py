from csv import excel

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:/Users/Praveen/PycharmProjects/Hybrid_Framework/Drivers/chromedriver95.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.quit()