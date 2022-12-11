import pytest,logging
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage_Actions import AddCustomer
from Utilities.readProperties import readConfig
from Utilities.customlogger import logGenerator as lg
from Utilities.module_mapping import driver_mapping
from selenium.webdriver.common.by import By
import string
import random

class Test_TableData_extraction:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = lg.log_utility(logging.DEBUG) # Logger

    @pytest.mark.sanity
    @pytest.mark.mytest
    def test_TableData_extraction(self,setup):
        self.logger.info("************* Test_Tabledata_Extraction **********")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("************input Username*************")
        self.driver.sendKeys(self.username, By.ID, self.lp.textbox_username_id)
        self.logger.info("************input Password*************")
        self.driver.sendKeys(self.password, By.ID, self.lp.textbox_password_id)
        self.logger.info("************clicking Login*************")
        self.driver.elementClick(By.XPATH, self.lp.button_login_xpath)
        self.logger.info("************Login Successfull*************")
        self.driver.wait(3)

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.driver.elementClick(By.XPATH ,self.addcust.lnkCustomers_menu_xpath)
        self.driver.elementClick(By.XPATH, self.addcust.lnkCustomers_menuitem_xpath)
        self.logger.info("************* Extracting customer info **********")
        rows = 1+ len(self.driver.getelements(By.XPATH,"//*[@id='customers-grid']/tbody/tr"))
        cols = 1 + len(self.driver.getelements(By.XPATH, "//*[@id='customers-grid']/tbody/tr[1]/td"))
        self.logger.info("rows = ,"+str(rows)+ ", columns ="+str(cols))
        for i in range(1,rows):
            for p in range(2,cols):
                value = self.driver.getText(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(i)+"]/td["+str(p)+"]")
                print(value, end="  ")
            print()
        self.driver.closebrowser()
        self.logger.info("******* Extracted data from table successfully **********")

