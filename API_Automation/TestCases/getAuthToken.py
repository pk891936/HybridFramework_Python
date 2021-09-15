import requests
import requests.auth

CLIENT_ID = "abcde"
CLIENT_SECRET = "12345"
TOKEN_URL = "https://api.example.com/oauth/access_token"
REDIRECT_URI = "https://www.getpostman.com/oauth2/callback"

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}
    response = requests.post(TOKEN_URL,
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]