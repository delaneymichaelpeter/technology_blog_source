#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Peter Delaney'
SITENAME = u'Peter Delaney Technical Notes'
SITEURL = ''

PATH = 'content'

#######################################################
# Added following Mathew Devaney Blog
# https://matthewdevaney.com/posts/2019/03/04/build-a-blog-with-pelican-and-python-pt-1-installation-theme/
#
OUTPUT_PATH = '../output'
THEME = 'theme'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n'],
}
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE  = 'monokai'
STATIC_PATH     = ['img', 'pdf' ]
PAGE_PATHS      = ['pages']
ARTICLE_PATH    = ['articles']
ARTICLE_URL     = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL        = 'pages/{slug}/'
PAGE_SAVE_AS    = 'pages/{slug}/index.html'
CATEGORY_URL    = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL         = 'tag/{slug}'
TAG_SAVE_AS     = 'tag/{slug}/index.html'

#######################################################


TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Delaney LinkedIn', 'http://linkedin.com/in/peterdelaney'),
         ('Delaney GitHub', 'http://github.com/delaneymichaelpeter'),
         ('Photo of Day', 'https://picsum.photos./200/300/'),
         ('You can modify those links in your elicanconf.py config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
