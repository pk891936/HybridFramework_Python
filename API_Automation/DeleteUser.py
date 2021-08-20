import requests

delete_url = "https://reqres.in/api/users/2"
response = requests.delete(delete_url)

print(response.status_code)
assert response.status_code == 204
