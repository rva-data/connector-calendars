===================
connector-calendars
===================

.. image:: https://badge.fury.io/py/connector-calendars.svg
    :target: https://badge.fury.io/py/connector-calendars

.. image:: https://travis-ci.org/rva-data/connector-calendars.svg?branch=master
    :target: https://travis-ci.org/rva-data/connector-calendars

.. image:: https://coveralls.io/repos/rva-data/connector-calendars/badge.svg?branch=master
    :target: https://coveralls.io/r/rva-data/connector-calendars?branch=master


Connector calendars is a Django application for tracking third-party calendars
via iCalendar feed and syncing events based on that feed. It relies on
`connector-events <https://github.com/rva-data/connector-events>`_ for managing
individual events themselves.

It was designed as a component for a 'connector' project, tracking events for a
community from multiple sources.

Documentation
-------------

The full documentation is at https://connector-calendars.readthedocs.org.

Quickstart
----------

Install connector-calendars::

    pip install connector-calendars

Then add events and calendars to your project's INSTALLED_APPS::

    INSTALLED_APPS = (
        'events',
        'calendars',
    )

After adding calendar feeds in the admin you can update them right from there,
or use the `read_calendars` management command to begin syncing them.
