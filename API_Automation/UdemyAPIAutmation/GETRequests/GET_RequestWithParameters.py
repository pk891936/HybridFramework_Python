import requests

paramdata = {'name':'testpython', 'email':'testvlapp@123.com'}
response = requests.get('https://httpbin.org/get', params=paramdata)
print(response.text)