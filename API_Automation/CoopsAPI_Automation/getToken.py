import requests
import requests.auth

CLIENT_ID = "MyAPI_Automate"
CLIENT_SECRET = "cb13c59a91da7fd4cb395dd663ba99e3"
TOKEN_URL = "http://coop.apps.symfonycasts.com/token"
REDIRECT_URI = "https://myapi.com"
token = None

def get_AuthToken():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials",
                 "redirect_uri": REDIRECT_URI}
    response = requests.post(TOKEN_URL,
                             auth=client_auth,
                             data=post_data)
    #print(response.text)
    token_json = response.json()
    token = token_json["access_token"]
    return token


def authorise():
    Authorize_URL = "http://coop.apps.symfonycasts.com/authorize?client_id=MyAPI_Automate&response_type="
    resp = requests.post(Authorize_URL + str(token))
    print(resp.text)