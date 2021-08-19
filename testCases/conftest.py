from selenium import webdriver
import pytest
from utilities.readProperties import readConfig

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        browserPath = readConfig.getBrowserPath("chrome")
        driver = webdriver.Chrome(browserPath)
        print("*************Launching Chrome Browser**************")
        driver.maximize_window()
    elif browser == 'firefox':
        browserPath = readConfig.getBrowserPath("firefox")
        driver = webdriver.Firefox()
        print("*************Launching Firefox Browser**************")
        driver.maximize_window()
    elif browser == 'edge':
        browserPath = readConfig.getBrowserPath("edge")
        driver = webdriver.Edge(browserPath)
        print("*************Launching Edge Browser**************")
        driver.maximize_window()
    else :
        browserPath = readConfig.getBrowserPath("ie")
        driver = webdriver.Ie(browserPath)
        print("*************Launching IE Browser**************")
        driver.maximize_window()
    return driver

def pytest_addoption(parser):       #this will get the values from CLI or hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):              #this will return browser value to setup
    return request.config.getoption("--browser")


####################### Pytest HTML Reports
def pytest_configure(config: "configure"):
    config._metadata['Project name'] = "nopcommerce"
    config._metadata['Module name'] = "Customer"
    config._metadata['Tester name'] = "Praveen"
    config._metadata['Test Environment'] = "Test"
@pytest.hookspec
@pytest.hookimpl
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


