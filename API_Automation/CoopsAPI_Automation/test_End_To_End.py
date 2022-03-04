import requests
import json , jsonpath
import allure
from utilities.customlogger import logGenerator
from utilities.readProperties import readConfig
from API_Automation.CoopsAPI_Automation.getToken import get_AuthToken

USER_ID= 2229
token = get_AuthToken()
logger =logGenerator.logGen()
Base_URL = readConfig.getCoopsAPI_URL()

@allure.severity(allure.severity_level.BLOCKER)
def test_post_Barn_unlock():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Barn-unlock*****************")
    print("Token: ", token)
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/barn-unlock"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200

@allure.severity(allure.severity_level.BLOCKER)
def test_post_toiletseat_down():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Toiletseat-down*****************")
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/toiletseat-down"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200


@allure.severity(allure.severity_level.BLOCKER)
def test_post_chickens_feed():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Chickens-feed*****************")
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/chickens-feed"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200


@allure.severity(allure.severity_level.BLOCKER)
def test_post_eggs_collect():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Eggs-collect*****************")
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/eggs-collect"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200


@allure.severity(allure.severity_level.BLOCKER)
def test_post_eggs_count():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Eggs-count*****************")
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/eggs-count"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200

@allure.severity(allure.severity_level.BLOCKER)
def test_post_eggs_count():
    logger.info("***************test_Coops_API*****************")
    logger.info("***************Post: Eggs-count*****************")
    Api_Url = Base_URL +"/api/"+str(USER_ID)+"/eggs-count"
    print("Post: ", str(Api_Url))
    response = requests.post(Api_Url, headers={'Authorization': 'Bearer '+token})
    logger.info(response.text)
    assert response.status_code == 200


