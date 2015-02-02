#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Santiago Chio'
SITENAME = u'Santiago Chio'
BANNER_SUBTITLE = u"A space to write about my work and interests."
SITEURL = ''

# Paths
PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Monterrey'

DEFAULT_LANG = 'en'

# Bootstrap theme
THEME = "/home/chio/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly'

# Header
BANNER = "/images/banner.jpg"
# SITELOGO = 'images/logo.jpg'
# SITELOGO_SIZE = 32
# FAVICON = 'images/favicon.png'

AVATAR = "/images/profile.jpg"
ABOUT_ME = "I build things with Python!"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

GITHUB_URL = 'https://github.com/schiob'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/schiob'),
          ('Facebook', 'https://facebook.com/schiob'),
          ('Twitter', 'https://twitter.com/schiob'),
          ('Google+', 'https://plus.google.com/u/0/+SantiagoChío'),
          )

# External services
DISQUS_SITENAME = 'schiobgithub'
DISQUS_SHORTNAME = 'schiobgithub'

DEFAULT_PAGINATION = 10

TAG_CLOUD_MAX_ITEMS = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
