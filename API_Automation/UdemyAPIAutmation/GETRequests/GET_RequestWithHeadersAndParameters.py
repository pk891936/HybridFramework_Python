import requests

headerdata = {'H1':'First', 'H2':'Second'}
paramdata = {'name':'testpython', 'email':'testvlapp@123.com'}
response = requests.get('https://httpbin.org/get', headers=headerdata, params=paramdata)
print(response.text)