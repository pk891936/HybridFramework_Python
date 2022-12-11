import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage_Action import SearchCustomer
from Utilities.readProperties import readConfig
from Utilities.customlogger import logGenerator
from Utilities.module_mapping import driver_mapping
from selenium.webdriver.common.by import By

class Test_SearchCustomerByName_005:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGenerator.logGen()  # Logger

    @pytest.mark.mytest
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
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

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.driver.elementClick(By.XPATH, self.addcust.lnkCustomers_menu_xpath)
        self.driver.elementClick(By.XPATH, self.addcust.lnkCustomers_menuitem_xpath)

        self.logger.info("************* searching customer by Name **********")
        self.searchcust = SearchCustomer(self.driver)
        self.driver.sendKeys("Victoria", By.ID, self.searchcust.txtFirstName_id)
        self.driver.sendKeys("Terces", By.ID, self.searchcust.txtLastName_id)
        self.driver.elementClick(By.ID, self.searchcust.btnSearch_id)
        time.sleep(5)
        status=self.searchcust.searchCustomerByName("Victoria Terces")
        self.driver.closebrowser()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")


