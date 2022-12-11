import json
import requests
import jsonpath

url = 'https://reqres.in/api/users?page=2'
response = requests.get(url)
print('************Status Code:',response.status_code)
assert response.status_code == 200
# Parse response to json format
json_response = json.loads(response.text)
print('***********Json Response *************\n', json_response)
# Parse value using json path
pages = jsonpath.jsonpath(json_response,'total_pages')
print('***********Pages: *************\n', pages)
print(pages[0])
assert pages[0] == 2
print("*********First Names of Get Response*********")
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name[0])