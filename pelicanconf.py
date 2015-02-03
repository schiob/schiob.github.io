#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Santiago Chio'
SITENAME = u'Santiago Chio'
BANNER_SUBTITLE = u"A space to write about my work and interests."
SITEURL = 'http://schiob.github.io'

# Paths
PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Monterrey'

DEFAULT_LANG = 'en'




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

##################### Exterior Services ############################
DISQUS_SITENAME = 'schiobgithub'
#DISQUS_SHORTNAME = 'schiobgithub'
#DISQUS_ID_PREFIX_SLUG = True

ADDTHIS_PROFILE = ' ra-54cedadb3f018eeb'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

####################### Theme-Specific Settings #########################
THEME = "/home/chio/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly'

# SITELOGO = 'images/logo.jpg'
# SITELOGO_SIZE = 32
# FAVICON = 'images/favicon.png'

AVATAR = "/images/profile.jpg"
ABOUT_ME = "I'm a programmer and a musician but over all I'm a constant learner.<p>Python lover. Data, Machine Learning and Cognitive Computing</p>"

BANNER = "/images/banner.jpg"


DEFAULT_PAGINATION = 10

TAG_CLOUD_MAX_ITEMS = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
