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

add_event_to_google_calendar_definition = {
  "name": "add_event_to_google_calendar",
  "description": "カレンダーに登録する関数です。",
  "parameters": {
    "type": "object",
    "properties": {
      "event_title": {
        "type": "string",
        "description": "予定のタイトル、予定のソース（分かる場合）"
      },
      "event_description": {
        "type": "string",
        "description": "予定の関連情報です。画像の読み取り結果の解釈や追加情報を入れてください。"
      },
      "event_location": {
        "type": "string",
        "description": "予定の実施場所"
      },
      "start_datetime": {
        "type": "string",
        "description": "（予定を繰り返す場合、最初の）予定を開始する日時（形式: ISO 8601, タイムゾーン: Asia/Tokyo）"
      },
      "end_datetime": {
        "type": "string",
        "description": "（予定を繰り返す場合、最初の）予定を終了する日時（形式: ISO 8601, タイムゾーン: Asia/Tokyo）"
      },
      "recurrence": {
        "type": "string",
        "description": "予定の繰り返し設定です。RRule(RFC5545)で表現されます。例: FREQ=WEEKLY;BYDAY=MO"
      }
    },
    "required": [
      "event_title",
      "start_datetime",
      "end_datetime"
    ]
  }
}
