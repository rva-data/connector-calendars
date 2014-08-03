#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import calendars

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = calendars.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='connector-calendars',
    version=version,
    description="""Django calendar ingestion app""",
    long_description=readme + '\n\n' + history,
    author='Ben Lopatin',
    author_email='ben@wellfire.co',
    url='https://github.com/rva-data/connector-calendars',
    packages=[
        'calendars',
    ],
    include_package_data=True,
    install_requires=[
        'connector-events',
    ],
    license="BSD",
    zip_safe=False,
    keywords='connector-calendars',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
