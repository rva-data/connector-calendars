from django.contrib import admin

from .models import CalendarFeed


class CalendarFeedAdmin(admin.ModelAdmin):
    actions = ['update_calendars']

    def update_calendars(self, request, queryset):
        for cal in queryset:
            cal.update()
        self.message_user(request, "Updated {0} feeds".format(queryset.count()))
    update_calendars.short_description = "Query feeds and update events"


admin.site.register(CalendarFeed, CalendarFeedAdmin)
