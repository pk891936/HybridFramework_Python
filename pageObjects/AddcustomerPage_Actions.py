import time
from selenium.webdriver.support.ui import Select
from utilities.module_mapping import driver_mapping
from selenium.webdriver.common.by import By


class AddCustomer(driver_mapping):
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//*[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "(//a[@href='/Admin/Customer/List'])[1]" ##"//*[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"

    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver_mapping):
        super().__init__(driver_mapping)
        self.driver = driver_mapping

    def setCustomerRoles(self,role):
        #self.driver.webScroll(self,"down")
        self.driver.elementClick(By.XPATH,self.txtcustomerRoles_xpath)
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.findelement(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.findelement(By.XPATH,self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.elementClick(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")
            time.sleep(2)
            #self.driver.elementClick(By.XPATH, self.txtcustomerRoles_xpath)
            self.listitem =self.driver.getelement(By.XPATH,self.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.findelement(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.findelement(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.findelement(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute(self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.getelement(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    #def setManagerOfVendor(self,value):
     #   self.driver.select_dropdown(By.XPATH,self.lstitemGuests_xpath, value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.elementClick(By.ID,self.rdMaleGender_id)
        elif gender=='Female':
            self.driver.elementClick(By.ID,self.rdFeMaleGender_id)
        else:
            self.driver.elementClick(By.ID,self.rdMaleGender_id)

