============
Installation
============

At the command line::

    $ pip connector-calendars

Installing in your project specific `virtualenv
<https://virtualenv.pypa.io/en/latest/virtualenv.html>_` is highly recommended.

Add `calendars` to your `INSTALLED_APPS` tuple::

    INSTALLED_APPS = (
        ...
        'calendars'.
    )

Add in the app URLs using the endpoint which makes the most sense for
your project::

    urlpatterns = patterns('',
        url(r'^calendars/', include('calendars.urls')),
    )