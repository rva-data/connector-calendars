import logging

from datetime import datetime
from django.db import models
from django.utils.text import slugify
from model_utils.models import TimeStampedModel

from events.models import Event
from .parsing import read_feed

logger = logging.getLogger(__name__)


def ustr(string):
    """
    Returns the Python version relevant string type
    """
    try:
        return unicode(string)
    except NameError:
        return str(string)


class ActiveCalendars(models.Manager):

    def get_queryset(self):
        """Returns the default Manager queryset"""
        return super(ActiveCalendars,
                     self).get_queryset().filter(is_active=True)

    def get_query_set(self):
        """Returns the default Manager queryset (DEPRECATED)"""
        return super(ActiveCalendars,
                     self).get_query_set().filter(is_active=True)


class CalendarFeed(TimeStampedModel):
    """
    Model class for managing iCalendar feeds of events
    """
    name = models.CharField(max_length=100)
    url = models.URLField(
        help_text="If the URL starts with webcal://<br/>...replace with http://")
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveCalendars()

    def __unicode__(self):
        return self.name

    def process_events(self, eventfeed):
        for ical_event in eventfeed:
            event_kwargs = {
                'name': ical_event['SUMMARY'],
                'slug': slugify(ustr(ical_event['SUMMARY'])),
                'description_markdown': ustr(ical_event.get('DESCRIPTION', u'')),
                'start': ical_event['DTSTART'].dt,
                'end': ical_event['DTEND'].dt,
                # 'location': ical_event['LOCATION'],
                'url': ical_event['url'],
            }
            if ical_event.get('GEO'):
                event_kwargs.update({
                    'latitude': ical_event['GEO'].latitude,
                    'longitude': ical_event['GEO'].longitude
                })
            event, created = Event.objects.get_or_create(
                    uid=ical_event['UID'], defaults=event_kwargs)
            if not created:
                for k in event_kwargs.keys():
                    setattr(event, k, event_kwargs[k])
                event.save()
            action = "Created" if created else "Updated"
            event.notes = "{0}\n{1} on {2}".format(
                    event.notes if event.notes else '',
                    action, datetime.now())
            event.save(update_fields=['notes'])

    def update(self):
        """
        This method should create or update Events after reading the
        CalendarFeed's ICS file.
        """
        events = read_feed(self.url)
        self.process_events(events)
        logger.debug("Updated the '{0}' calendar".format(self.name))
