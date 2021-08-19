import pytest
from selenium.webdriver import *
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customlogger import logGenerator

class Test_001_Login:

    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = logGenerator.logGen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginPageTitle(self,setup):
        self.logger.info("************test_LoginPageTitle*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************Loaded URL*************")
        self.driver.implicitly_wait(3)
        self.logger.info("************Verifying LoginPage Title*************")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("************test_LoginPageTitle Passed*************")
            self.driver.quit()
            assert True
        else :
            self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle.png")
            self.logger.error("************test_LoginPageTitle Failed*************")
            self.driver.quit()
            assert False


    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("************test_Login*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************Loaded URL*************")
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.logger.info("************input Username*************")
        self.lp.setUserName(self.username)
        self.logger.info("************input Password*************")
        self.lp.setPassword(self.password)
        self.logger.info("************clicking Login*************")
        self.lp.clickLogin()
        self.logger.info("************Login Successfull*************")
        self.driver.implicitly_wait(3)
        self.logger.info("************Verifying HomePage Title*************")
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************test_Login Failed*************")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Login.png")
            self.logger.error("************test_Login Failed*************")
            self.driver.quit()
            assert False


