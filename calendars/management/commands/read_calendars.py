from django.core.management.base import BaseCommand

from ...models import CalendarFeed


class Command(BaseCommand):
    """
    Fetches and parses all of the stored calendar feeds
    """
    def handle(self, *args, **options):
        for calendar in CalendarFeed.active.all():
            calendar.update()
