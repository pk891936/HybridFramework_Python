import pytest
from selenium.webdriver import *
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customlogger import logGenerator
from Utilities import ExcelUtils


class Test_002_Login_DDT:
    # path = readConfig.getTestDataPath()

    baseURL = readConfig.getApplicationURL()
    logger = logGenerator.logGen()
    def test_Login_DDT(self, setup):
        self.logger.info("************Test_002_Login_DDT**************")
        self.logger.info("************test_Login*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************Loaded URL*************")
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        path = readConfig.getTestDataPath()
        row = ExcelUtils.getRowCount(path, "Sheet1")

        ExcelUtils.writeData(path, "Sheet1", 1, 5, "salary")
        for r in range(2, row + 1):
            username = ExcelUtils.readData(path, "Sheet1", r, 1)
            password = ExcelUtils.readData(path, "Sheet1", r, 2)
            exp = ExcelUtils.readData(path, "Sheet1", r, 3)
            list_status = []

            self.logger.info("************input Username*************")
            self.lp.setUserName(username)
            self.logger.info("************input Password*************")
            self.lp.setPassword(password)
            self.logger.info("************clicking Login*************")
            self.lp.clickLogin()
            self.logger.info("************Login Successfull*************")
            self.driver.implicitly_wait(3)
            self.logger.info("************Verifying HomePage Title*************")
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if exp == "Pass":
                    self.logger.info("************Passed*************")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                    assert True
                elif exp == "Fail":
                    self.logger.info("************Failed*************")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title == "Dashboard / nopCommerce administration":
                if exp == "Pass":
                    self.logger.info("************Failed*************")
                    self.lp.clickLogout()
                    list_status.append("Fail")
                    assert True
                elif exp == "Fail":
                    self.logger.info("************Passed*************")
                    self.lp.clickLogout()
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("**********test_Login_DDT Passed***********")
            self.driver.quit()
            assert True
        else:
            self.logger.info("**********test_Login_DDT Failed***********")
            self.driver.quit()
            assert False
        self.logger.info("***************test_Login_DDT completed***********************")
