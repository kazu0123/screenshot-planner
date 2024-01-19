from fastapi.routing import APIRouter

from auth_google import CALENDAR_ID, calendar_service
from calendar_event import CalendarEvent

router = APIRouter()

@router.post('/create-event')
def create_event(calendar_event: CalendarEvent):
    insert_event = {
        'summary': calendar_event.event_title,
        'location': calendar_event.event_location,
        'description': calendar_event.event_description,
        'start': {
            'dateTime': calendar_event.start_datetime,
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': calendar_event.end_datetime,
            'timeZone': 'Asia/Tokyo',
        },
        'recurrence': calendar_event.recurrence
    }

    insert_event = calendar_service.events().insert(
        calendarId=CALENDAR_ID,
        body=insert_event
    ).execute()

    return insert_event['htmlLink']
