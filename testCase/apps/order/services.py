import os.path
import pickle

import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


class Auth:

    def __init__(self, client_secret_filename, scopes):
        self.client_secret = client_secret_filename
        self.scopes = scopes
        self.flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(self.client_secret, self.scopes)
        self.flow.redirect_uris ='http://localhost:8080/'
        self.creds = None


    def get_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.client_secret, self.scopes)
        self.creds = flow.run_local_server(port=8080)
        return self.creds
        # authorization_url, state = self.flow.authorization_url(
        #     # Enable offline access so that you can refresh an access token without
        #     # re-prompting the user for permission. Recommended for web server apps.
        #     access_type='offline',
        #     # Enable incremental authorization. Recommended as a best practice.
        #     include_granted_scopes='true')
        # return authorization_url #, state
    #     # The file token.pickle stores the user's access and refresh tokens, and is
    #     # created automatically when the authorization flow completes for the first
    #     # time.
    #     if os.path.exists('token.pickle'):
    #         with open('token.pickle', 'rb') as token:
    #             self.creds = pickle.load(token)
    #
    #     # If there are no (valid) credentials available, let the user log in.
    #     if not self.creds or not self.creds.valid:
    #         if self.creds and self.creds.expired and self.creds.refresh_token:
    #             self.creds.refresh(Request())
    #         else:
    #             flow = InstalledAppFlow.from_client_secrets_file(self.client_secret, self.scopes)
    #             self.creds = flow.run_local_server(port=8080)
    #         # Save the credentials for the next run
    #     with open('token.pickle', 'wb') as token:
    #         pickle.dump(self.creds, token)
    #     return self.creds