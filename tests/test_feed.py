import os

from datetime import datetime
from pytz import timezone
from django.test import TestCase

from calendars.parsing import read_feed, get_events


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
