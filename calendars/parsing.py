import requests

from datetime import datetime
from pytz import timezone
from icalendar import Calendar, Event
from django.conf import settings


def read_feed(feed_url):
    """
    """
    response = requests.get(feed_url)
    cal = Calendar.from_ical(response.content)
    events = get_events(cal)
    # EVENT({'STATUS': 'CONFIRMED', 'DTSTAMP': <icalendar.prop.vDDDTypes object
    # at 0x101523390>, 'DESCRIPTION': 'Gangplank RVA\nFriday, December 13 at
    # 11:00 AM\n\nThis is for people interested in having conversations
    # regarding real world issues in running a small business (or starting a
    # new one). Bring your lunc...\n\nDetails:
    # http://www.meetup.com/GangplankRVA/events/qgfkkgyrqbrb/', 'CREATED':
    # <icalendar.prop.vDDDTypes object at 0x101523490>, 'URL':
    # 'http://www.meetup.com/GangplankRVA/events/qgfkkgyrqbrb/', 'SUMMARY':
        # 'Gangplank RVA: Entrepreneurs Friday Lunch Meeting', 'LAST-MODIFIED':
        # <icalendar.prop.vDDDTypes object at 0x101523510>, 'DTEND':
        # <icalendar.prop.vDDDTypes object at 0x101523410>, 'DTSTART':
        # <icalendar.prop.vDDDTypes object at 0x1015233d0>, 'GEO':
        # <icalendar.prop.vGeo object at 0x1015234d0>, 'CLASS': 'PUBLIC',
        # 'UID': 'event_qgfkkgyrqbrb@meetup.com'})
    return events


def is_valid_event(item, start, end):
    """
    Return True if the item from a calendar is an event and it is between the
    specified range of start and end times.
    """
    if not isinstance(item, Event):
        return False
    if start and item['DTSTART'].dt < start:
        return False
    if end and item['DTEND'].dt > end:
        return False
    return True


def get_events(calendar, start=None, end=None, tz=settings.TIME_ZONE):
    """
    Return events from an icalendar.cal.Calendar.
    """
    if start is None:
        start = datetime.now(timezone(tz))
    return [e for e in calendar.walk() if is_valid_event(e, start, end)]
