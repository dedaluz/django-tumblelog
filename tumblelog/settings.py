from django.conf import settings
from django.utils.translation import ugettext as _


POSTS_PER_PAGE = getattr(settings, 'TUMBLELOG_POSTS_PER_PAGE', 10)

POST_TYPES = getattr(settings, 'TUMBLELOG_POST_TYPES', [
    'tumblelog.contrib.text.Article',
    'tumblelog.contrib.text.Text',
    'tumblelog.contrib.file.File',
    'tumblelog.contrib.photo.Image',
])
OEMBED_DEFAULT_CACHE_AGE = getattr(settings, \
    'TUMBLELOG_OEMBED_DEFAULT_CACHE_AGE', 86400)
TWITTER_LANGUAGE = getattr(settings, 'TUMBLELOG_TWITTER_LANGUAGE', 'en')
TWITTER_WIDTH = getattr(settings, 'TUMBLELOG_TWITTER_WIDTH', 325)
FLICKR_WIDTH = getattr(settings, 'TUMBLELOG_FLICKR_WIDTH', 640)
SOUNDCLOUD_COLOR = getattr(settings, 'TUMBLELOG_SOUNDCLOUD_COLOR', '')
TEXTFIELD_HELP_TEXT = _(getattr(settings, 'TUMBLELOG_TEXTFIELD_HELP_TEXT', ''))

RSS_TITLE = _(getattr(settings, 'TUMBLELOG_RSS_TITLE', ''))
RSS_LINK = getattr(settings, 'TUMBLELOG_RSS_LINK', '')
RSS_DESCRIPTION = _(getattr(settings, 'TUMBLELOG_RSS_DESCRIPTION', ''))
RSS_NUM = getattr(settings, 'TUMBLELOG_RSS_NUM', 20)
