import requests
import json , jsonpath
import allure
from utilities.customlogger import logGenerator
from utilities.readProperties import readConfig


@allure.severity(allure.severity_level.BLOCKER)
def test_get_People():
    logger =logGenerator.logGen()
    logger.info("***************GET:Final Student Details After Update*****************")
    finaldetails_URL = "http://0.0.0.0:5000/api/people"
    response = requests.get(finaldetails_URL)
    logger.info(response.text)








