import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json',
             scopes=["https://www.googleapis.com/auth/youtube.readonly"]
   )

flow.run_local_server(port=8080, authorization_prompt_message="consent")

credentials = flow.credentials()

print(credentials.to_json())

api_key = os.environ.get("YT_API_KEY")

youtube = build("youtube","v3", developerKey=api_key)

request = youtube.playlistItems().list(
    part="status", playlistId="PLW9rmNobMa6aeZIsFuZJhMZNEdAY"
)

response = request.execute()
print(response)