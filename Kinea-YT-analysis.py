from googleapiclient.discovery import build
import pandas as pd

api_key = 'AIzaSyCyETXDwxDF5tLb2A_n-oUr0lbE74JxXNA'

list_id = ['PLpbom12S-UaJEDmUaFfWLws317OUKNceE']

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

# Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)

def get_list_stats(youtube, list_stats):
    

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
)
response = request.execute()

print(response)

print('teste')
