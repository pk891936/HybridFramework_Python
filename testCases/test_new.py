import pytest,logging,allure
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage_Actions import AddCustomer
from utilities.readProperties import readConfig
from utilities.customlogger import logGenerator as lg
from utilities.module_mapping import driver_mapping
from selenium.webdriver.common.by import By
import string
import random

class Test_001_Alert:

    alertURL = "http://demo.guru99.com/test/delete_customer.php"
    windowURL = "http://demo.guru99.com/popup.php"
    frameURL = "http://demo.guru99.com/test/guru99home/"
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = lg.logGen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)

    def test_Alert(self,setup):
        self.logger.info("************* Test_Alert **********")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.alertURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("************input Custormer*************")
        self.driver.sendKeys("Praveen", By.NAME, "cusid")
        self.logger.info("************clicking Delete*************")
        self.driver.elementClick(By.NAME, "submit")
        self.driver.wait(3)
        self.driver.switchto("alert", "dismiss")
        self.driver.elementClick(By.NAME, "submit")
        self.driver.wait(3)
        self.driver.switchto("alert","accept")
        self.logger.info("************Alert handled Successfull*************")
        self.driver.closebrowser()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
    def test_window(self, setup):
        self.logger.info("************* Test_Alert **********")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.windowURL)

        self.driver.elementClick(By.XPATH, "/html/body/p/a")
        self.driver.switchto("window", "child")
        self.driver.wait(3)
        self.driver.sendKeys("praveenkmr151@hmail.com", By.NAME, "emailid")
        self.driver.wait(3)
        self.driver.switchto("window", "parent")
        self.driver.wait(3)
        self.logger.info("************window handled Successfull*************")
        self.driver.closebrowser()

    def test_frame(self, setup):
        self.logger.info("************* Test_Alert **********")
        self.wb = setup
        self.driver = driver_mapping(self.wb)
        self.driver.navigate(self.frameURL)
        self.driver.switchto("frame", "a077aa5e")
        self.driver.wait(3)
        self.driver.elementClick(By.XPATH, "html / body / a / img")
        self.driver.wait(3)
        self.driver.switchto("window", "child")
        self.driver.closeWindow()
        self.driver.switchto("window", "parent")
        self.driver.wait(3)
        self.driver.switchto("frame", "default")
        self.driver.elementClick(By.XPATH, "//*[@href='http://www.guru99.com/software-testing.html']")
        self.driver.wait(3)
        self.logger.info("************Frame handled Successfull*************")
        self.driver.closebrowser()



