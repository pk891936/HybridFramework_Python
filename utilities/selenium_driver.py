from selenium.webdriver.common.by import By
######### For Explicit wait import below
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.customlogger import logGenerator as lg
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from utilities.readProperties import readConfig

import cx_Oracle
import re
##################################################
import time
import logging

class SeleniumDriver():


    # Create object instance for logging
    log = lg.log_utility(logging.DEBUG)

    # Set init value for driver and Constants
    def __init__(self,driver):
        self.driver = driver
        #self.constants = Constants()
        self.UIvalue = None
        self.DBvalue = None
        self.finalquery = None
        self.rawquery = None

    def map_webelement(self,keyword):
        if keyword == 'id':
            result = None
            result = "By.ID"
            return result
        elif keyword == 'xpath':
            result = None
            result = "By.XPATH"
            return result
        elif keyword == 'link_text':
            result = None
            result = "By.LINK_TEXT"
            return result
        elif keyword == 'partial_link_text':
            result = None
            result = "By.PARTIAL_LINK_TEXT"
            return result
        elif keyword == 'name':
            result = None
            result = "By.NAME"
            return result
        elif keyword == 'tag_name':
            result = None
            result = "By.TAG_NAME"
            return result
        elif keyword == 'class_name':
            result = None
            result = By.CLASS_NAME
            return result
        elif keyword == 'css_selector':
            result = None
            result = By.CSS_SELECTOR
            return result
        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")
            return False



    # Method for browser navigation
    def navigate(self,datavalue):
        try:
            self.driver.get(datavalue)
            self.driver.maximize_window()
            self.log.info("Navigated to "+datavalue)
            return True
        except:
            self.log.error("Navigation failed")
            return False

    # Get web element based on the locator value
    def getelement(self,locatortype,locator):
        try:
            element = self.driver.find_element(locatortype,locator)
            self.log.info("Element found")
        except:
            self.log.info("Element not found")

        return element

    def getelements(self,locatortype,locator):
        try:
            element = self.driver.find_elements(locatortype,locator)
            self.log.info("Elements found")
        except:
            self.log.info("Elements not found")

        return element


    # Method to find web element occurance
    def findelement(self,locatortype,locator):
        try:

            elementtofind = None
            elementtofind = self.driver.find_element(locatortype,locator)
            self.log.info("Element found")
            # If element occurance found then return True
            if len(elementtofind) > 0:
                return True
            else:
                return False
                self.log.info("Element not found")
        except:
            self.log.info("Some error occured, element not found")
            return False

        # Method to find web element occurance
    def findelements(self, locatortype, locator):
        try:

            elementtofind = None
            elementtofind = self.driver.find_elements(locatortype, locator)
            self.log.info("Element found")
            # If element occurance found then return True
            if len(elementtofind) > 0:
                return True
            else:
                return False
                self.log.info("Element not found")
        except:
            self.log.info("Some error occured, element not found")
            return False

    # Method to wait for an element
    def waitforelement(self,locatortype,locator):
        try:
            elementowait = None
            nwait=None
            # wait object with certain seconds and ignoring conditions
            nwait = WebDriverWait(self.driver,10,poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # Wait for an element until the expected conditions are met
            elementowait = nwait.until(EC.presence_of_element_located(locatortype,locator))
            return elementowait

        except Exception as e:
            self.log.info("Element was not found, wait limit exceeded: "+str(e.args))
            return False



    # Method to perform element click
    def elementClick(self,locatortype,locator):
        try:
            self.getelement(locatortype,locator).click()
            self.log.info("Element clicked")
            return True
        except:
            self.log.error("Element not clicked")
            return False

    # Method to enter/type text
    def sendKeys(self,data,locatortype,locator):
        try:
            self.getelement(locatortype,locator).clear()
            self.getelement(locatortype,locator).send_keys(data)
            self.log.info("Data entered")
            return True
        except:
            self.log.info("Cannot send data to the element")
            return False

    # Method to capture screenshot
    def capturescreen(self):

        try:
            filename = "Scrnshot"+"_"+str(round(time.time()*1000))+".png"
            folder_location = readConfig.getScreenshotPath()
            destination = folder_location+filename
            self.driver.save_screenshot(destination)
            self.log.info("Captured screenshot")
            return True
        except NotADirectoryError:
            self.log.info("Capture screenshot failed")
            return False

    def capturescreen_Allure(self):
        try:
            return self.driver.get_screenshot_as_png()
            self.log.info("Captured screenshot")
        except BaseException as msg:
            self.log.info(msg)


    # Method to get page title
    def getTitle(self):
        return self.driver.title

    def getText(self,locatortype,locator):
        return self.driver.find_element(locatortype,locator).text

    # Method for scrolling of web page
    def webScroll(self,direction):

        try:
            if direction == 'up':
                self.driver.execute_script("window.scrollBy(0,-1000);")
                return True
            elif direction == 'down':
                self.driver.execute_script("window.scrollBy(0,1000);")
                return True
            elif direction == 'right':
                self.driver.execute_script("window.scrollBy(1000,0);")
                return True
            else:
                self.driver.execute_script("window.scrollBy(-1000,0);")
                return True
        except:
            self.log.error("Scrolling failed")
            return False


    # Method to Select value from the dropdown

    def select_dropdown(self, locatortype, locator, type, datavalue):
        try:
            drop_down = self.driver.find_element(locatortype,locator)
            sel_element = Select(drop_down)
            if type == "index":
                sel_element.select_by_index(datavalue)
            elif type == "value":
                sel_element.select_by_value(datavalue)
            elif type == "visible_text":
                sel_element.select_by_visible_text(datavalue)
            return True
        except:
            self.log.error("Dropdown selection failed")
            return False



    # Method to Select radio button
    def select_radio(self,locatortype,locator,datavalue):
        try:
            #update locator locatortype with parameter datavalue
            ulocator = locator.format(datavalue)
            nradio = self.driver.find_element(locatortype,ulocator)
            nradio.click()
            ulocator = ""
            return True
        except:
            self.log.error("Select radio button failed")
            return False

    # Method to Select checkbox
    def select_checkbox(self, locatortype, locator, datavalue):

        try:
            #update locator locatortype with parameter datavalue
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(locatortype,ulocator)
            isSelected = ncheckbox.is_selected()
            if not isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            self.log.error("Select checkbox failed")
            return False


    # Method to unselect checkbox
    def unselect_checkbox(self,locatortype,locator,datavalue):

        try:
            #update locator locatortype with parameter datavalue
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(locatortype,ulocator)
            isSelected = ncheckbox.is_selected()
            if isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            self.log.error("Unselect of checkbox failed")
            return False

    # Method to wait
    def wait(self,datavalue):
        try:
            nseconds = int(float(datavalue))
            time.sleep(nseconds)
            return True
        except:
            self.log.error("Wait for failed")
            return False

    # Method to verify Text, enabled, selected, displayed, exists, title
    def verify_title(self, value):
        try:
            title = str(self.getTitle())
            self.log.info(title)
            if title == value:
                return True
            else:
                return False
        except:
            self.log.error("Verify failed")
            return False

    def verify(self,property,value,locatortype,locator):
        try:
            if property == "text":
                UI_Text = None
                UI_Text = self.driver.find_element(locatortype,locator).text
                if str(UI_Text) == str(value):
                    return True
                else:
                    return False
            elif property == "enabled":
                enable_flag = None
                enable_flag = self.driver.find_element(locatortype,locator).is_enabled()
                if str(enable_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "selected":
                select_flag = None
                select_flag = self.driver.find_element(locatortype, locator).is_selected()
                if str(select_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "displayed":
                display_flag = None
                display_flag = self.driver.find_element(locatortype, locator).is_displayed()
                if str(display_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "exists":
                exist_flag = None
                exist_flag = self.findelement(locator)
                if str(exist_flag) == str(value):
                    return True
                else:
                    return False

        except:
            self.log.error("Verify failed")
            return False

    # Method to move cursor to an element
    def moveto(self,locatortype,locator):
        try:
            element = None
            element = self.driver.find_element(locatortype,locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        except:
            self.log.error("Cursor Move to element failed")
            return False

    # Method to drag and drop element from source to destination
    def dragndrop(self,locatortype,locator,targetvalue):
        try:
            from_element = self.driver.find_element(locatortype,locator)
            to_element = self.driver.find_element(locatortype,targetvalue)
            action = ActionChains(self.driver)
            action.drag_and_drop(from_element,to_element).perform()
            return True
        except:
            self.log.error("Drag and drop failed")
            return False

    # Method to close browser
    def closebrowser(self):
        try:
            self.driver.quit()
            return True
        except:
            self.log.error("Close browser failed")
            return False

        # Method to close current window
    def closeWindow(self):
        try:
            self.driver.close()
            return True
        except:
            self.log.error("Close window failed")
            return False

    def switchto(self,property,value):
        try:
            #if not value.isalpha():
               # value = int(float(value))
               # value = value - 1
            #else:
               # value = str(value)

            if property == "window" and value == "parent":
                #current_window = self.driver.window_handles(0)
                #print(current_window)
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.log.info("Switched to: " +str(value), " " + str(property))
                return True
            elif property == "window" and value == "child":
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.log.info("Switched to: " + str(value) + str(property))
                return True
            elif property == "window" :
                self.driver.switch_to.window(self.driver.window_handles[int(value)])
                self.log.info("Switched to: " + str(property))
                return True
            elif property == "frame":
                if value == "default":
                    self.driver.switch_to.default_content()
                    return True
                else:
                    self.driver.switch_to.frame(value)
                    return True
            elif property == "alert":
                alertpop = self.driver.switch_to.alert
                if value == "accept":
                    alertpop.accept()
                    return True
                elif value == "dismiss":
                    alertpop.dismiss()
                    return True
                else:
                    alert_text = str(alertpop.text)
                    if  value in alert_text:
                        return True
                    else:
                        return False
        except BaseException as msg:
            self.log.error(msg)
            self.log.error("Failed to switch to: "+ str(property))
            return False



    # Get UI value in a variable
    def savedata(self,locatortype,locator,value):
        try:
            value = None
            value = str(self.driver.find_element(locatortype,locator).text).strip()
            self.UIvalue = value
            #print("UI value is "+self.UIvalue)
            return True
        except:
            self.log.error("Failed to get data value from UI")
            return False

        # Connect to DB via oracle string

    def dbconnect(self,Conn_String):
        try:
            self.conn = cx_Oracle.Connection(Conn_String)
            #link cursor  to  the connection
            self.curr = self.conn.cursor()
            return True
        except:
            self.log.error("DB connection failed")
            return False


    # Get draft query
    def draftquery(self,value):
        try:
            self.rawquery = str(value)
            #print("query is "+str(value))
            return True
        except:
            self.log.error("Failed to get draft query")
            return False

    # Concat draft query
    def concat(self,value):
        try:
            self.finalquery = self.rawquery + " " + str(value)
            self.rawquery = self.finalquery
            return True
        except:
            self.log.error("Failed to concat query")
            return False

    # Execute the query
    def executequery(self):
        try:
            if self.finalquery is None:
                self.resultset = self.curr.execute(self.rawquery)
            else:
                self.resultset = self.curr.execute(self.finalquery)
            return True
        except:
            self.log.error("Execute query failed")
            return False

    # Get db value
    def getdbvalue(self,value):
        try:
            value = None
            self.result_list = self.resultset.fetchall()

            for rows in self.result_list:
                value = str(rows[0])
                self.DBvalue = value
                #print("DB value "+self.DBvalue)
            self.curr.close()
            self.conn.close()
            return True

        except:
            self.log.error("Failed to get db value into a variable")
            return False


    # compare db and UI value
    def compare(self):
        try:
            # Using regex match only alphanumeric characters excluding special characters
            # and replacing with blank character
            nDBvalue = re.sub("[^\w\.]", "", self.DBvalue)
            nUIvalue = re.sub("[^\w\.]", "", self.UIvalue)
            # compare db and UI value
            if nDBvalue == nUIvalue:
                return True
            else:
                return False
        except:
            self.log.error("Comparison between DB and UI value failed")
            return False


            # Method to perform element click

    def doubleClick(self, locatortype, locator):
        try:
            element = None
            element = self.getelement(locatortype,locator)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
            return True
        except:
            self.log.error("Double Click on the element failed")
            return False

    def execute(self, value):
        try:
            self.driver.execute_script("arguments[0].click();", value)
            #self.execute_script("arguments[0].click();", value)
            return True
        except BaseException as msg:
            self.log.exception(msg)
            self.log.error("Execute Element failed")
            return False









































