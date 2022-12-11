import requests

headerdata = {'H1':'First', 'H2':'Second'}
response = requests.get('https://httpbin.org/get', headers=headerdata)
print(response.text)