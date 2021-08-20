import requests
import json , jsonpath
from utilities.customlogger import logGenerator

def test_AddNew_Student():
    logger =logGenerator.logGen()
    logger.info("***************test_AddNew_Student*****************")
    logger.info("***************Post:Add New Student*****************")
    App_Url = "http://thetestingworldapi.com/api/studentsDetails"
    f= open("C://Users//Praveen//PycharmProjects//Hybrid_Framework//API_Automation//JsonFiles//AddNewStudent.json",'r')
    request_json = json.loads(f.read())
    response = requests.post(App_Url,request_json)
    id = jsonpath.jsonpath(response.json(),"id")
    #print(response.text)
    print(id)

    logger.info("***************Post:Add Student Technical Skills*****************")
    tech_API_URL = "http://thetestingworldapi.com/api/technicalskills"
    f = open("C://Users//Praveen//PycharmProjects//Hybrid_Framework//API_Automation//JsonFiles//TechDetails.json",'r')
    request_json = json.loads(f.read())
    request_json["id"] = int(id[0])
    request_json["st_id"] = id[0]
    response = requests.post(tech_API_URL, request_json)
    #print(response.text)

    logger.info("***************Post:Add Student Address*****************")
    address_API_URL = "http://thetestingworldapi.com/api/addresses"
    f = open("C://Users//Praveen//PycharmProjects//Hybrid_Framework//API_Automation//JsonFiles//Address.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    response = requests.post(address_API_URL, request_json)

    logger.info("***************GET:Final Student Details*****************")
    finaldetails_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
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
    Updateaddress_API_URL = "http://thetestingworldapi.com/api/addresses/" + str(id[0])
    f = open("C://Users//Praveen//PycharmProjects//Hybrid_Framework//API_Automation//JsonFiles//UpdateAddress.json", 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = int(id[0])
    response = requests.post(address_API_URL, request_json)
    logger.info(response.text)

    logger.info("***************GET:Final Student Details After Update*****************")
    finaldetails_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(finaldetails_URL)
    logger.info(response.text)








