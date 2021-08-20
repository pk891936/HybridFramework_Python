import requests
import json, jsonpath

#API URLS
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response)

#Display response content
#print(response.content)

#Parse response to json
json_response = json.loads(response.text)
#print(json_response)

#Fetch value using jsonpath
total_page= jsonpath.jsonpath(json_response,"total_pages")
print(total_page)
assert total_page[0]== 2
