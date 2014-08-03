import os

from datetime import datetime, timedelta
from pytz import timezone
from django.test import TestCase

from events.models import Event
from ..models import CalendarFeed
from ..parsing import read_feed, get_events


class FeedTests(TestCase):
    """
    When provided with an ICS feed URL, the app should be able to request the
    feed content, parse the events from the feed, check for existing matching
    events in the system based on UID, update those events, and add new events
    where no match is found.
    """

    def test_invalid_feed(self):
        """Ensure a helpful exception is raised"""
        # Mock requests
        self.assertRaises(Exception, read_feed, "http://www.example.com/badfeed")

    def test_valid_feed(self):
        """Ensure a dictionary of event data is returned"""
        pass

    def test_loads_events(self):
        """The parsing function should return events"""
        from icalendar import Calendar
        test_cal = os.path.join(os.path.dirname(__file__), "feed.ics")
        with open(test_cal, "r") as f:
            cal = Calendar.from_ical(f.read())
        self.assertEqual(18, len(get_events(cal,
            start=datetime(2013, 10, 10, tzinfo=timezone('America/New_York')))))
        self.assertEqual(17, len(get_events(cal,
            start=datetime(2013, 10, 12, tzinfo=timezone('America/New_York')))))


class EventTests(TestCase):

    def setUp(self):
        """
        Includes one event which occurred in the past and so need not be
        updated, one event for which there is a match and the information
        should be updated.
        """
        today = datetime.today()
        self.old_event = Event(name="Old event", slug="old-event",
                start=(today - timedelta(days=1)),
                uid='event_dxczvgyrnbdc@meetup.com')
        self.unchanged_event = Event(name="Unchanged event",
                slug="unchanged-event",
                start=(today - timedelta(days=1)),
                uid='event_qgfkkgyrnbhc@meetup.com')
        self.update_event = Event(name="Update event", slug="update-event",
                start=(today - timedelta(days=1)),
                uid='event_dxczvgyrnbmc@meetup.com')

    def test_add_event(self):
        """Ensure a new event is added"""
        self.fail()

    def test_update_event(self):
        """Updated event with matching UID should be updated"""
        self.fail()
