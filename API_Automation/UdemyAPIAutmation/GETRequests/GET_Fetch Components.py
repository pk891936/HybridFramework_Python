import json
import requests
import jsonpath

url = 'https://reqres.in/api/users?page=2'
response = requests.get(url)
print('************Status Code:',response.status_code)
assert response.status_code == 200
print('************Content***************\n', response.content)

# Fetch response Headers
print('***********Headers*************\n', response.headers)
print(response.headers.get('Content-Type'))
print(response.headers.get('Server'))

# Fetch Cookies
print('************Cookies***************\n',response.cookies)

#Fetch Encoding
print('************Cookies***************\n',response.encoding)
#Fetch Elapsed time
print('************Elapsed Time:',response.elapsed)