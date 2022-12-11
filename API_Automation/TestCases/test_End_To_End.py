import requests
import json
import jsonpath
import allure
from Utilities.customlogger import logGenerator
from Utilities.readProperties import readConfig


@allure.severity(allure.severity_level.BLOCKER)
def test_AddNew_Student():
    logger =logGenerator.logGen()
    Base_URL = readConfig.getAPI_URL()
    logger.info("***************test_AddNew_Student*****************")
    logger.info("***************Post:Add New Student*****************")
    App_Url = Base_URL+"/api/studentsDetails"
    JsonFilePath=readConfig.getJsonFilePath()
    f= open(JsonFilePath+"//AddNewStudent.json",'r')
    payload_json = json.loads(f.read())
    response = requests.post(App_Url,payload_json)
    print(response.text)
    print(response.status_code)
    resp_json = json.loads(response.text)
    print("*****Response*********")
    print(resp_json)
    print("**************************************************")
    assert response.status_code == 200
    #assert resp_json['id'] is not None
    id = jsonpath.jsonpath(resp_json,"id")

    print(id)

    logger.info("***************Post:Add Student Technical Skills*****************")
    tech_API_URL = Base_URL+"/api/technicalskills"
    f = open(JsonFilePath+"//TechDetails.json",'r')
    request_json = json.loads(f.read())
    print("*****Request*********")
    print(request_json)
    print("**************************************************")
    request_json["id"] = int(id[0])
    request_json["st_id"] = id[0]
    response = requests.post(tech_API_URL, request_json)
    print(response.text)
    assert response.status_code == 200

    logger.info("***************Post:Add Student Address*****************")
    address_API_URL = Base_URL+"/api/addresses"
    f = open(JsonFilePath+"//Address.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    response = requests.post(address_API_URL, request_json)
    print(response.status_code,"--Post:status code")
    assert response.status_code == 200

    logger.info("***************GET:Final Student Details*****************")
    finaldetails_URL = Base_URL+"/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(finaldetails_URL)
    print(response.status_code, "--Get: status code")
    assert response.status_code == 200
    print(response.headers)
    logger.info(response.text)

    # logger.info("***************DELETE: Student Details*****************")
    # delete_URL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    # response = requests.delete(delete_URL)
    # logger.info(response.text)
    # print(response.text)
    # assert response.status_code == 405
    # logger.info("***************Test Case Completed*****************")

    logger.info("***************PUT:Update Student Address*****************")
    Updateaddress_API_URL = Base_URL+"/api/addresses/" + str(id[0])
    f = open(JsonFilePath+"//UpdateAddress.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    print(request_json)
    response = requests.put(address_API_URL, request_json)
    print("Update Status Code:", response.status_code)
    logger.info(response.text)
    assert response.status_code == 405


    logger.info("***************GET:Final Student Details After Update*****************")
    finaldetails_URL = Base_URL+"/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(finaldetails_URL)
    logger.info(response.text)
    resp_json = response.json()
    assert response.status_code == 200
    print("*******************Final response******************************************")
    a = resp_json['data']
    print(resp_json)
    print(a)











