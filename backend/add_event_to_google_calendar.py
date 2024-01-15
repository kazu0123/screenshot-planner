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

service = build('calendar', 'v3', credentials=creds)

def add_event_to_google_calendar(
    start_datetime: str, # ISO 8601
    end_datetime: str, # ISO 8601
    event_title: str,
    recurrence: str = "", # RRule(RFC5545)
    event_description:str = "",
    event_location: str = "",
):
    event = {
        'summary': "【このイベントは無視してください。】" + event_title,
        'location': event_location,
        'description': "このイベントはアプリ開発のためのテストで作成されました。このイベントは削除して問題ありません。\n\n" + event_description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Asia/Tokyo',
        },
        "recurrence":recurrence
    }
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return "success"
