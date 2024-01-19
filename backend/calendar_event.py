from pydantic import BaseModel, Field

class CalendarEvent(BaseModel):
    event_title: str = Field(
        description="予定、タスクのタイトルを入れてください。",
        examples=["バンタン授業 python応用"] )
    event_description:str = Field(
        description="予定の関連情報、追加情報を入れてください。関連するURLなどもあれば入れてください。",
        examples=["講師：喜多村先生"],
        default="" )
    event_location: str = Field(
        description="予定の実施場所を入れてください。分かれば住所も入れてください。オンラインの場合、サービス名か「オンライン」と入れてください。",
        examples=["バンタン名古屋1号館 402教室"],
        default="" )
    start_datetime: str = Field(
        description="（予定を繰り返す場合、最初の）予定を開始する日時を入れてください。形式はISO 8601、タイムゾーンはAsia/Tokyoにしてください。",
        examples=["2023-12-04T09:30:00.000+09:00"] )
    end_datetime: str = Field(
        description="（予定を繰り返す場合、最初の）予定を終了する日時を入れてください。形式はISO 8601、タイムゾーンはAsia/Tokyoにしてください。",
        examples=["2023-12-04T12:20:00.000+09:00"] )
    recurrence: str = Field(
        description="予定の繰り返し設定を入れてください。形式はRRule(RFC5545)にしてください。",
        examples=["FREQ=WEEKLY;BYDAY=WE"] )
