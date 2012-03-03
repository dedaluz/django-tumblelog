from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.fields import OEmbedURLField
from tumblelog.models import BaseOembedVideo


class BaseOembedVideoWithThumbnail(BaseOembedVideo):
    """
    Abstraction of fields and properties specific to an oEmbed video object
    with a thumbnail.
    """
    thumbnail_url = models.URLField(_('Thumbnail'), max_length=1024, \
        null=True, blank=True, editable=False)
    thumbnail_width = models.IntegerField(_('Thumbnail Width'), null=True, \
        blank=True, editable=False)
    thumbnail_height = models.IntegerField(_('Thumbnail Height'), null=True, \
        blank=True, editable=False)

    class Meta:
        abstract = True

    @property
    def thumbnail(self):
        return {
            'url': self.thumbnail_url,
            'width': self.thumbnail_width,
            'height': self.thumbnail_height,
        }


class YouTube(BaseOembedVideoWithThumbnail):
    """
    Post type for an a YouTube video, with metadata and embed code pulled
    directly from the source using YouTube's oEmbed API:

    http://apiblog.youtube.com/2009/10/oembed-support.html
    """
    youtube_url = OEmbedURLField(_('YouTube URL'), max_length=1024)
    youtube_user = models.CharField(_('Uploader\'s Username'), null=True, \
        blank=True, max_length=512, editable=False)
    youtube_user_url = models.URLField(_('Uploader\'s YouTube Channel'), \
        null=True, blank=True, max_length=1024, editable=False)
    youtube_title = models.CharField(_('YouTube Title'), max_length=512, \
        null=True, blank=True, editable=False)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'YouTube Video'
        verbose_name_plural = 'YouTube Videos'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        change_form_template = 'admin/youtube_change_form.html'
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'youtube_url', 'caption',)
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

    oembed_endpoint = 'http://www.youtube.com/oembed'
    oembed_schema = [
        'http://*youtube.com/watch*',
        'http://*.youtube.com/v/*',
        'https://*youtube.com/watch*',
        'https://*.youtube.com/v/*',
        'http://youtu.be/*',
        'http://*.youtube.com/user/*',
        'http://*.youtube.com/*#*/*',
        'http://m.youtube.com/watch*',
        'http://m.youtube.com/index*',
        'http://*.youtube.com/profile*',
        'http://*.youtube.com/view_play_list*',
        'http://*.youtube.com/playlist*'
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('author_name', 'youtube_user',),
        ('author_url', 'youtube_user_url',),
        ('title', 'youtube_title',),
        ('html', 'embed',),
        'thumbnail_url',
        'thumbnail_width',
        'thumbnail_height',
    )

    @property
    def oembed_resource(self):
        return self.youtube_url


class Vimeo(BaseOembedVideoWithThumbnail):
    """
    Post type for an a Vimeo video, with metadata and embed code pulled
    directly from the source using Vimeo's oEmbed API:

    https://vimeo.com/api/docs/oembed
    """
    vimeo_url = OEmbedURLField(_('Vimeo URL'), max_length=1024)
    vimeo_user = models.CharField(_('Uploader\'s Username'), max_length=512, \
        null=True, blank=True, editable=False)
    vimeo_user_url = models.URLField(_('Uploader\'s Vimeo Profile'), \
        max_length=1024, null=True, blank=True, editable=False)
    vimeo_title = models.CharField(_('Vimeo Title'), max_length=512, \
        null=True, blank=True, editable=False)
    vimeo_video_id = models.IntegerField(_('Vimeo ID'), max_length=9, \
        null=True, blank=True, editable=False)
    duration = models.IntegerField(_('Duration'), max_length=6, null=True, \
        blank=True, editable=False)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Vimeo Video'
        verbose_name_plural = 'Vimeo Videos'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        change_form_template = 'admin/vimeo_change_form.html'
        fieldsets = (
            (None, {
                'fields': ('title', 'vimeo_url', 'caption',)
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

    oembed_endpoint = 'http://vimeo.com/api/oembed.json'
    oembed_schema = [
        'http://www.vimeo.com/groups/*/videos/*',
        'http://www.vimeo.com/*',
        'http://vimeo.com/groups/*/videos/*',
        'http://vimeo.com/*',
        'http://vimeo.com/m/#/*',
        'https://www.vimeo.com/groups/*/videos/*',
        'https://www.vimeo.com/*',
        'https://vimeo.com/groups/*/videos/*',
        'https://vimeo.com/*',
        'https://vimeo.com/m/#/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('author_name', 'vimeo_user',),
        ('author_url', 'vimeo_user_url',),
        ('title', 'vimeo_title',),
        ('video_id', 'vimeo_video_id',),
        ('html', 'embed',),
        'thumbnail_url',
        'thumbnail_width',
        'thumbnail_height',
        'duration',
    )

    @property
    def oembed_resource(self):
        return self.vimeo_url
