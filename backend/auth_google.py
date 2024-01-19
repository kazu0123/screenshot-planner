import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

load_dotenv(verbose=True)

# Google Calendar APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/calendar']

# カレンダーID（Googleカレンダーの設定から確認できます）
CALENDAR_ID = os.environ.get('CALENDAR_ID')

creds = None
token_json_path = 'secrets/token.json'
credentials_json_path = 'secrets/credentials.json'

# 以前の認証情報があればそれを読み込みます
if os.path.exists(token_json_path):
    creds = Credentials.from_authorized_user_file(token_json_path)

# 認証情報が無効または存在しない場合は新しい認証情報を取得します
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_json_path, SCOPES)
        creds = flow.run_local_server(port=0)
    # 取得した認証情報を保存します
    with open(token_json_path, 'w') as token:
        token.write(creds.to_json())

calendar_service = build('calendar', 'v3', credentials=creds)
