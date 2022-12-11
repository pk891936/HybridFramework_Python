import json
import requests
import jsonpath

url = 'https://reqres.in/api/users/2'
response = requests.delete(url)
print('************Status Code:',response.status_code)
assert response.status_code == 204

#get_res = requests.get('https://reqres.in/api/users?page=2')
#json_get_res = json.loads(get_res.text)
#print(json_get_res)