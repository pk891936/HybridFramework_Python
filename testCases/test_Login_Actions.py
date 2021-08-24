import pytest
import logging
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customlogger import logGenerator as lg
from utilities.module_mapping import driver_mapping

class Test_001_Login:

    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = lg.log_utility(logging.DEBUG)

    @pytest.mark.sanity
    @pytest.mark.mytest
    def test_LoginPageTitle(self,setup):
        self.logger.info("************test_LoginPageTitle*************")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.baseURL)
        #self.driver.get(self.baseURL)
        self.logger.info("************Loaded URL*************")
        self.driver.wait(3)
        self.logger.info("************Verifying LoginPage Title*************")
        condition = self.driver.verify_title("Your store. Login")

        if condition == True :
            self.logger.info("************test_LoginPageTitle Passed*************")
            self.driver.closebrowser()
            assert True
        else :
            self.driver.capturescreen()
            self.logger.error("************test_LoginPageTitle Failed*************")
            self.driver.closebrowser()
            assert False

    @pytest.mark.mytest
    def test_Login(self, setup):
        self.logger.info("************test_Login*************")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.baseURL)
        self.logger.info("************Loaded URL*************")
        self.driver.wait(3)
        self.lp = LoginPage(self.driver)
        self.logger.info("************input Username*************")
        self.driver.sendKeys(self.username,By.ID,self.lp.textbox_username_id)
        self.logger.info("************input Password*************")
        self.driver.sendKeys(self.password, By.ID, self.lp.textbox_password_id)
        self.logger.info("************clicking Login*************")
        self.driver.elementClick(By.XPATH,self.lp.button_login_xpath)
        self.logger.info("************Login Successfull*************")
        self.driver.wait(3)
        self.logger.info("************Verifying HomePage Title*************")
        condition = self.driver.verify_title("Dashboard / nopCommerce administration")

        if condition == True:
            self.logger.info("************test_HomePage title Passed*************")
            self.driver.closebrowser()
            assert True
        else:
            self.driver.capturescreen()
            self.logger.error("************test_HomePage title Failed*************")
            self.driver.closebrowser()
            assert False







