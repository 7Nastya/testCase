import shutil
from django.http import HttpResponse
from django.views import View
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
from .services import Auth

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = '/home/nas/PycharmProjects/testCase/credrntials.json'


class TestCaseView(View):

    def get(self, request, *args, **kwargs):
        credentials = Auth(client_secret_filename=SERVICE_ACCOUNT_FILE, scopes=SCOPES).get_credentials()
        service = build('drive', 'v3', credentials=credentials)
        file_id = '1IeyaDsmjTpcc6QjCH6wuFLtRbz6u8e40'
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO('test.xlsx', mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%" % int(status.progress() * 100))
        # The file has been downloaded into RAM, now save it in a file
        # fh.seek(0)
        # with open('test.csv', 'wb') as f:
        #     shutil.copyfileobj(fh, f, length=131072)
        return HttpResponse("OK")


class TestAPIView(View):
    def get(self):
        x = 0
        return HttpResponse("OK")
