import requests

from datetime import datetime
from django.conf import settings
from icalendar import Calendar, Event
from pytz import timezone


def read_feed(feed_url):
    """
    Generates an events list based on a calendar URL

    :param feed_url: valid URL for an iCalendar feed
    :returns: list of icalendar Events
    """
    response = requests.get(feed_url)
    cal = Calendar.from_ical(response.content)
    return get_events(cal)


def is_valid_event(item, start, end):
    """
    Determines whether an event is valid for inclusion in a list of events
    based on whether it falls within a specified range of times.

    :param item: an Event
    :param start: datetime for when the valid range should start
    :param end: datetime for when the valid range should end
    :returns: boolean, is the event within time range
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
    Returns a list of events from an icalendar Calendar based on an optional
    window of time

    :param calendar: an icalendar Calendar
    :param start: an optional datetime for when the valid range should start
    :param end: an optional datetime for when the valid range should end
    :returns: list of icalendar Events
    """
    if start is None:
        start = datetime.now(timezone(tz))
    return [e for e in calendar.walk() if is_valid_event(e, start, end)]
