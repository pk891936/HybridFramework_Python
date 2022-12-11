import json
import requests
import jsonpath

url = 'https://reqres.in/api/users/2'
f = open("../Input_Payloads/UpdateData.json", 'r')
json_payload = json.loads(f.read())
response = requests.put(url,json_payload)
print('************Response:',response.content)
print('************Status Code:',response.status_code)
assert response.status_code == 200
# Parse response to json format
json_res_post = json.loads(response.text)
updated = jsonpath.jsonpath(json_res_post,'updatedAt')
print("********Data updated :",updated)
jobupdated = jsonpath.jsonpath(json_res_post,'job')
print("********Data updated :",jobupdated)
get_res = requests.get('https://reqres.in/api/users/2')
json_get_res = json.loads(get_res.text)
print(json_get_res)
updatedjob = jsonpath.jsonpath(json_get_res,'job')
print("********Job Updated :",updatedjob)