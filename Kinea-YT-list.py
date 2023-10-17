import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

api_key = 'AIzaSyCyETXDwxDF5tLb2A_n-oUr0lbE74JxXNA'

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Make an API request to retrieve playlist items
playlist_id = 'PLpbom12S-UaJEDmUaFfWLws317OUKNceE'
request = youtube.playlistItems().list(
    part='snippet',
    maxResults=400,  # Set the number of results you want
    playlistId=playlist_id
)
response = request.execute()

# Initialize an empty list to store the data
data = []

# Process the response
for item in response['items']:
    video_id = item['snippet']['resourceId']['videoId']
    video_response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()

    title = item['snippet']['title']
    likes = video_response['items'][0]['statistics']['likeCount']
    views = video_response['items'][0]['statistics']['viewCount']

    data.append({
        'Title': title,
        'Likes': likes,
        'Views': views
    })

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('playlist_data.csv', index=False)

df