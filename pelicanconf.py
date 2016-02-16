#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean Pierre Roussaffa'
SITENAME = u'JP'
SITEURL = 'http://jproussaffa.pythonanywhere.com'

PATH = 'content'

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = u'fr'
DATE_FORMATS = {
    #'en': '%a, %d %b %Y',
    'en': '%d %m %Y',
    'jp': '%Y-%m-%d(%a)',
    'fr': '%d %m %Y'}

PLUGIN_PATHS = 
['../pelican-plugins/',
'pelican-flickr',
]
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'sitemap',
           #'pelican-flickr',
           ]

LOAD_CONTENT_CACHE = False

THEME = "pure-single-jp"

EXTRA_TEMPLATES_PATHS = ['../pelican-themes/flickr/',]

DEFAULT_LANG = 'fr'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

COVER_IMG_URL = '/../../images/.jpg'
PROFILE_IMG_URL = '/../../images/photo.jpg'
TAGLINE = 'Colporter la terre à mesure'
#FAVICON_URL - Set the favicon image
DISQUS_SITENAME = "jproussaffa"
DISQUS_ON_PAGES = True
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')
MENUITEMS = (
  #('Geomatic', 'pages/project-manager-gis-administrator-and-spatial-analyst.html'),
  #('Image Sound Prod', 'pages/we-are-prod.html'),('Claire Cousergue', 
  #  'pages/claire-cousergue-camerawoman-location-manager.html'),
  ('Gallerie Photo', 'pages/my-albums.html'),
  ('Archives','archives.html')
  )

STATIC_PATHS = ['images']

#  generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PDF_GENERATOR = True

FLICKR_API_KEY = '5cf424d08c3247ca52634c9b63d95562'
FLICKR_API_SECRET = '1e5a0b89562b0df6'
FLICKR_USER = '138559734@N07'


# Blogroll
#LINKS = ((,),(,))

# Social widget
SOCIAL = (#('soundcloud', 'https://soundcloud.com/yogis-record'),
          ('flickr','https://www.flickr.com/photos/138559734@N07'),
          #('youtube', 'https://www.youtube.com/channel/UCK6L4K87OB9cQMdMZRnz5hg'),
		  #('map-marker','https://www.openstreetmap.org/user/goym@p/history'),
		  #('github-square','https://github.com/yougis'),
      ('rss-square',FEED_ALL_ATOM))

DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
