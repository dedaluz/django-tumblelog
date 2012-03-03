import re

from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.choices import TWITTER_LANGUAGE_CHOICES
from tumblelog.fields import OEmbedURLField
from tumblelog.models import BaseOembedRich
from tumblelog.settings import TWITTER_LANGUAGE, TWITTER_WIDTH


class Tweet(BaseOembedRich):
    """
    Post type for an a Tweet, with metadata and embed code pulled directly from
    the source using Twitter's oEmbed API:

    https://dev.twitter.com/docs/api/1/get/statuses/oembed
    """
    tweet_url = OEmbedURLField(_('Tweet URL'), max_length=1024)
    hide_media = models.BooleanField(_('Hide media?'), default=False)
    hide_thread = models.BooleanField(_('Hide thread?'), default=False)
    maxwidth = models.IntegerField(_('Maximum Width'),
        max_length=3,
        default=TWITTER_WIDTH
    )
    language = models.CharField(_('Language'),
        default=TWITTER_LANGUAGE,
        max_length=2,
        choices=TWITTER_LANGUAGE_CHOICES
    )
    twitter_user = models.CharField(_('Author\'s Name'),
        max_length=512,
        editable=False
    )
    twitter_user_url = models.URLField(_('Author\'s Twitter Profile'),
        max_length=512,
        editable=False
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = _('Tweet')
        verbose_name_plural = _('Tweets')

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        change_form_template = 'admin/tweet_change_form.html'
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'tweet_url', 'caption',)
            }),
            ('Tweet Settings', {
                'classes': ('collapse',),
                'fields': (
                    'hide_media',
                    'hide_thread',
                    'language',
                    'maxwidth',
                ),
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published',)
            }),
        )
        list_display = (
            'title',
            'date_published',
        )
        list_filter = (
            filters.PubliclyVisibleListFilter,
            filters.PublicationDateListFilter,
            filters.StatusListFilter,
        )
        prepopulated_fields = {
            'slug': ('title',)
        }
        search_fields = [
            'title',
            'slug',
            'caption',
        ]

    oembed_endpoint = 'https://api.twitter.com/1/statuses/oembed.json'
    oembed_schema = [
        'http://twitter.com/#!/*/status/*',
        'https://twitter.com/#!/*/status/*',
        'http://twitter.com/*/status/*',
        'https://twitter.com/*/status/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        ('author_name', 'twitter_user',),
        ('author_url', 'twitter_user_url',),
        'cache_age',
        ('url', 'tweet_url',),
        ('html', 'embed'),
        ('width', 'width'),
    )

    @property
    def oembed_resource(self):
        return self.tweet_url

    @property
    def oembed_endpoint_params(self):
        return {
            'hide_media': str(self.hide_media).lower(),
            'hide_thread': str(self.hide_thread).lower(),
            'lang': self.language.lower(),
            'maxwidth': self.maxwidth
        }

    @property
    def twitter_username(self):
        """
        Returns the poster's Twitter username.

        This method is necessarily fragile, as Twitter's oEmbed response does
        not return this property.
        """
        return re.search(r'([^\/]+)$', self.twitter_user_url).groups()[0]
