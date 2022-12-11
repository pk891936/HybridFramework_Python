import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import *
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customlogger import logGenerator

class Test_001_Login:

    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = logGenerator.logGen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
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
            self.driver.implicitly_wait(2)
            allure.attach(self.driver.get_screenshot_as_png(),name="test_LoginPageTitle.png", attachment_type=AttachmentType.PNG)
            #self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle.png")
            self.logger.error("************test_LoginPageTitle Failed*************")
            self.driver.quit()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_skip(self):
        pytest.skip("**********this test is skipped**********")


    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
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
        if act_title == "Dashboard / nopCommerce administrationss":
            self.logger.info("************test_Login Failed*************")
            self.driver.quit()
            assert True
        else:
            #self.driver.save_screenshot(".\\Screenshots\\test_Login.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HomePageTitle.png",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("************test_Login Failed*************")
            self.driver.quit()
            assert False


