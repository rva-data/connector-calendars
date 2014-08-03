from datetime import datetime, timedelta
from django.test import TestCase

from events.models import Event


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
