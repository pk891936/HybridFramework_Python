import requests
import json , jsonpath
from utilities.customlogger import logGenerator
from utilities.readProperties import readConfig

def test_AddNew_Student():
    logger =logGenerator.logGen()
    Base_URL = readConfig.getAPI_URL()
    logger.info("***************test_AddNew_Student*****************")
    logger.info("***************Post:Add New Student*****************")
    App_Url = Base_URL+"/api/studentsDetails"
    JsonFilePath=readConfig.getJsonFilePath()
    f= open(JsonFilePath+"//AddNewStudent.json",'r')
    request_json = json.loads(f.read())
    response = requests.post(App_Url,request_json)
    id = jsonpath.jsonpath(response.json(),"id")
    #print(response.text)
    print(id)

    logger.info("***************Post:Add Student Technical Skills*****************")
    tech_API_URL = Base_URL+"/api/technicalskills"
    f = open(JsonFilePath+"//TechDetails.json",'r')
    request_json = json.loads(f.read())
    request_json["id"] = int(id[0])
    request_json["st_id"] = id[0]
    response = requests.post(tech_API_URL, request_json)
    #print(response.text)

    logger.info("***************Post:Add Student Address*****************")
    address_API_URL = Base_URL+"/api/addresses"
    f = open(JsonFilePath+"//Address.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    response = requests.post(address_API_URL, request_json)

    logger.info("***************GET:Final Student Details*****************")
    finaldetails_URL = Base_URL+"/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(finaldetails_URL)
    logger.info(response.text)

    # logger.info("***************DELETE: Student Details*****************")
    # delete_URL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    # response = requests.delete(finaldetails_URL)
    # logger.info(response.text)
    # print(response.text)
    # assert response.status_code == 405
    # logger.info("***************Test Case Completed*****************")

    logger.info("***************PUT:Update Student Address*****************")
    Updateaddress_API_URL = Base_URL+"/api/addresses/" + str(id[0])
    f = open(JsonFilePath+"//UpdateAddress.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    response = requests.post(address_API_URL, request_json)
    logger.info(response.text)

    logger.info("***************GET:Final Student Details After Update*****************")
    finaldetails_URL = Base_URL+"/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(finaldetails_URL)
    logger.info(response.text)








