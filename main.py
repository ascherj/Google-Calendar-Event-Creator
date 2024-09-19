import datetime
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up OAuth 2.0 flow
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None

# If modifying these SCOPES, delete the token.json file
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(google.auth.default())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

service = build('calendar', 'v3', credentials=creds)

# Base parameters for the event
calendar_id = 'primary'
start_date = datetime.date(2024, 9, 19)  # Starting date
num_weeks = 10  # Number of weeks to create events for

for week in range(num_weeks):
    event_date = start_date + datetime.timedelta(weeks=week)

    event = {
        'summary': f'<EVENT NAME>',  # Increment the event title
        'start': {
            'date': event_date.isoformat(),  # All-day event (date only)
            'timeZone': 'America/Denver',  # Adjust for your timezone
        },
        'end': {
            'date': (event_date + datetime.timedelta(days=1)).isoformat(),
            'timeZone': 'America/Denver',
        },
        'recurrence': [
            # This will be ignored for this script since we are creating individual events.
        ],
    }

    # Insert the event
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f'Event created: {event_result["summary"]} on {event_result["start"]["date"]}')
