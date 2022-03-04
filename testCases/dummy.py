#name dob gender
import requests,json
import jsonpath

payload= { 'name':"Praveen",
           'dob':"04-06-1993",
           'gender':"Male"

}
payload = json.loads()
response = requests.post("API_Url",payload)
resp_json = response.json()
id = jsonpath.jsonpath(resp_json['id'])

print(response.status_code)
print(response.text)
assert  response.status_code =='201'
assert resp_json['student_id'] is not None