#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tortoise ORM team'
SITENAME = 'Tortoise ORM'
SITESUBTITLE = 'Tortoise ORM news & releases'
SITEURL = 'https://tortoise.github.io'

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
CUSTOM_MENUITEMS = (
    ('Documentation', 'https://tortoise-orm.readthedocs.io/'),
    ('Chat on Gitter', 'https://gitter.im/tortoise/community'),
    ('Source', 'https://github.com/tortoise'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ['images']
ARTICLE_PATHS = ['', 'releases']

TYPOGRIFY = True

THEME = "cait"

## path to logo for nav menu (optional)
LOGO = 'tortoise.png'

# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

EXTRA_PATH_METADATA = {
    'images/tortoise.ico': {'path': 'favicon.ico'},
}
