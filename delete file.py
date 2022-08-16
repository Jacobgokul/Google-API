from oauth2client import file, client, tools
from googleapiclient import discovery
import httplib2
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import date, datetime, timedelta

access_token = None 
client_id = #Client Id take from OAuth 2.0 Client IDs.
client_secret = #Cient secret take from OAuth 2.0 Client IDs.
refresh_token = #take token from oauthplayground by autheticating.
token_expiry = None
token_uri = "https://accounts.google.com/o/oauth2/token"
user_agent = 'YourAgent/1.0'

credentials = client.GoogleCredentials(access_token, client_id, client_secret, refresh_token, token_expiry, token_uri, user_agent)

http = credentials.authorize(httplib2.Http())
credentials.refresh(http)
service = build('drive', 'v3', http=http)
folder_id = #Give folder id take from url in google-drive
query = f"parents = '{folder_id}'"
req = service.files().list(q=query)
resp = req.execute(http=http)
lst_file = resp['files'] #File be like dict of dict, So used key to take files values.

dates = datetime.today()
d = dates.strftime('%Y-%m-%d')
#delete files older than 7days
def delete():
    q = datetime.strptime(d, "%Y-%m-%d") 
    for u in lst_file:
        o = u['createdTime'].split('T')[0] #CreatedTime will be like '22-07-2021T05:45:34 so splited the date alone
        p = datetime.strptime(o,"%Y-%m-%d") #Converted to date format to compare 
        old_date = q - timedelta(days=7) #Took 7days old date using timedelta by subtracting with today's date
        if old_date > p:
            file_id = u['id']
            service.files().delete(fileId=file_id).execute(http=http)

delete()

#Done by Gokul