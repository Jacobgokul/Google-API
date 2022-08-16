import os
from oauth2client import file, client, tools
from googleapiclient import discovery
import httplib2
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime, timedelta
import time


path = '' #specify path ends with '/' where server have backup dbs.
folder_id = '' #ID of folder in gdrive.
access_token = None 
client_id = '' #Client Id take from OAuth 2.0 Client IDs.
client_secret = '' #Cient secret take from OAuth 2.0 Client IDs.
refresh_token = '' #take token from oauthplayground by autheticating.
token_expiry = None
token_uri = "https://accounts.google.com/o/oauth2/token"
user_agent = 'YourAgent/1.0'
credentials = client.GoogleCredentials(access_token, client_id, client_secret, refresh_token, token_expiry, token_uri, user_agent)
http = credentials.authorize(httplib2.Http())
credentials.refresh(http)
service = build('drive', 'v3', http=http)

# upload file to gdrive
def upload():
    for file in os.listdir(path):
        db = os.path.realpath(file)
        file_path, filename = os.path.split(db)
        file = path+filename
        today_date = datetime.today().date()
        file_date = datetime.fromtimestamp(os.path.getctime(file)).date()
        if today_date == file_date:
            file_metadata = {'name': file,'parents': [folder_id]}
            media = MediaFileUpload(file, mimetype='application/zip',resumable=True)
            file = service.files().create(body=file_metadata,media_body=media,fields='id').execute(http=http)

if __name__ == '__main__':
    upload()

#Done by Gokul