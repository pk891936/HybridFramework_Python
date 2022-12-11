import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage_Action import SearchCustomer
from Utilities.readProperties import readConfig
from Utilities.customlogger import logGenerator as lg
from selenium.webdriver.common.by import By
from Utilities.module_mapping import driver_mapping

class Test_SearchCustomerByEmail_004:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = lg.logGen()  # Logger

    @pytest.mark.mytest
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
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

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.driver.elementClick(By.XPATH, self.addcust.lnkCustomers_menu_xpath)
        self.driver.elementClick(By.XPATH, self.addcust.lnkCustomers_menuitem_xpath)

        self.logger.info("************* searching customer by emailID **********")
        self.searchcust = SearchCustomer(self.driver)
        self.driver.sendKeys("victoria_victoria@nopCommerce.com", By.ID, self.searchcust.txtEmail_id)
        self.driver.elementClick(By.ID, self.searchcust.btnSearch_id)
        time.sleep(5)
        status=self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.closebrowser()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")


