import pytest,logging
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage_Actions import AddCustomer
from utilities.readProperties import readConfig
from utilities.customlogger import logGenerator as lg
from utilities.module_mapping import driver_mapping
from selenium.webdriver.common.by import By
import string
import random

class Test_003_AddCustomer:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = lg.log_utility(logging.DEBUG) # Logger

    @pytest.mark.sanity
    @pytest.mark.mytest
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
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
        self.driver.elementClick(By.XPATH, self.addcust.btnAddnew_xpath)

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.driver.sendKeys(self.email, By.XPATH, self.addcust.txtEmail_xpath)
        self.driver.sendKeys("test123", By.XPATH, self.addcust.txtPassword_xpath)
        self.driver.sendKeys("Praveen", By.XPATH, self.addcust.txtFirstName_xpath)
        self.driver.sendKeys("Kumar", By.XPATH, self.addcust.txtLastName_xpath)
        self.driver.sendKeys("test123", By.XPATH, self.addcust.txtPassword_xpath)
        self.driver.sendKeys("test123", By.XPATH, self.addcust.txtPassword_xpath)
        self.driver.sendKeys("7/05/1995", By.XPATH, self.addcust.txtDob_xpath)  # Format: D / MM / YYY
        self.addcust.setGender("Male")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")

        self.driver.sendKeys("busyQA",By.XPATH,self.addcust.txtCompanyName_xpath)
        self.driver.sendKeys("This is for testing.........", By.XPATH, self.addcust.txtAdminContent_xpath)
        self.driver.elementClick(By.XPATH,self.addcust.btnSave_xpath)
        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.getText(By.TAG_NAME,"body")

        #print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
            assert True
        else:
            self.driver.capturescreen()
            self.logger.error("************Add customer Test Failed*************")
            assert False

        self.driver.closebrowser()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
