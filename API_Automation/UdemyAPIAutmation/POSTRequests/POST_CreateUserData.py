import json
import requests
import jsonpath

url = 'https://reqres.in/api/users'
f = open("../Input_Payloads/CreateData.json", 'r')
json_payload = json.loads(f.read())
response = requests.post(url,json_payload)
print('************Response:',response.content)
print('************Status Code:',response.status_code)
assert response.status_code == 201
# Parse response to json format
json_res_post = json.loads(response.text)
user_id = jsonpath.jsonpath(json_res_post,'id')
print("********Data Created ID:",user_id[0])
get_res = requests.get('https://reqres.in/api/users/'+str(user_id[0]))
json_get_res = json.loads(get_res.text)
print(json_get_res)