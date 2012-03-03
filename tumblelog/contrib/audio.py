from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.choices import SOUNDCLOUD_HEIGHT_CHOICES
from tumblelog.fields import OEmbedURLField
from tumblelog.models import BaseOembedRich
from tumblelog.settings import SOUNDCLOUD_COLOR


class Rdio(BaseOembedRich):
    """

    """
    rdio_url = OEmbedURLField(_('Rdio URL'),
        max_length=1024,
        help_text=_('Can be the URL of an album, track, or playlist')
    )
    rdio_title = models.CharField(_('Rdio Title'),
        max_length=512,
        null=True,
        blank=True,
        editable=False
    )
    thumbnail_url = models.URLField(_('Thumbnail'), max_length=1024, \
        null=True, blank=True, editable=False)
    thumbnail_width = models.IntegerField(_('Thumbnail Width'), null=True, \
        blank=True, editable=False)
    thumbnail_height = models.IntegerField(_('Thumbnail Height'), null=True, \
        blank=True, editable=False)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Rdio'
        verbose_name_plural = 'Rdio Players'

    class TumblelogMeta:
        date_hierarchy = 'date_published'
        list_display = (
            'title',
            'date_published',
        )
        search_fields = [
            'title',
            'slug',
            'caption',
        ]
        list_filter = (
            filters.PubliclyVisibleListFilter,
            filters.PublicationDateListFilter,
            filters.StatusListFilter,
        )
        change_form_template = 'admin/rdio_change_form.html'
        fieldsets = (
            (None, {
                'fields': ('title', 'rdio_url', 'caption',)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published',)
            }),
        )
        prepopulated_fields = {
            'slug': ('title',)
        }

    oembed_endpoint = 'http://www.rdio.com/api/oembed/'
    oembed_schema = [
        'http://www.rdio.com/*',
        'http://rd.io/x/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('title', 'rdio_title',),
        ('html', 'embed',),
        'thumbnail_url',
        'thumbnail_width',
        'thumbnail_height',
    )

    @property
    def oembed_resource(self):
        return self.rdio_url

    @property
    def thumbnail(self):
        return {
            'url': self.thumbnail_url,
            'width': self.thumbnail_width,
            'height': self.thumbnail_height,
        }


class SoundCloud(BaseOembedRich):
    """

    """
    soundcloud_url = OEmbedURLField(_('Soundcloud URL'),
        max_length=1024,
        help_text=_('Can be the URL of an track, set, group, or user')
    )
    soundcloud_title = models.CharField(_('Soundcloud Title'),
        max_length=512,
        null=True,
        blank=True,
        editable=False
    )
    soundcloud_description = models.CharField(_('Soundcloud Description'),
        max_length=8192,
        null=True,
        blank=True,
        editable=False
    )
    maxwidth = models.IntegerField(_('Width'),
        max_length=4,
        null=True,
        blank=True,
        help_text=_('Measured in pixels'),
    )
    maxheight = models.CharField(_('Height'),
        max_length=3,
        choices=SOUNDCLOUD_HEIGHT_CHOICES,
        blank=True,
        null=True,
        help_text=_('Only valid for tracks'),
    )
    color = models.CharField(_('Color'),
        max_length=6,
        default=SOUNDCLOUD_COLOR,
        blank=True,
        null=True,
        help_text=_(
            'The primary color of the widget as a hex triplet, e.g. "ff0066"'
        ),
    )
    auto_play = models.BooleanField(_('Autoplay on load?'),
        default=False
    )
    show_comments = models.BooleanField(_('Show SoundCloud\'s timed comments?'),
        default=False
    )
    html5_player = models.BooleanField(_('Use the HTML5 player?'),
        default=True
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Soundcloud'
        verbose_name_plural = 'Soundcloud Players'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        change_form_template = 'admin/soundcloud_change_form.html'
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'soundcloud_url', 'caption',)
            }),
            ('Settings', {
                'classes': ('collapse',),
                'fields': (
                    ('maxwidth', 'maxheight',),
                    'color',
                    'auto_play',
                    'show_comments',
                    'html5_player',
                )
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published',)
            }),
        )
        list_display = (
            'title',
            'date_published',
            'status',
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
            'soundcloud_title',
            'soundcloud_description',
        ]

    oembed_endpoint = 'http://soundcloud.com/oembed'
    oembed_schema = [
        'http://soundcloud.com/*',
        'http://snd.sc/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('title', 'soundcloud_title',),
        ('description', 'soundcloud_description',),
        ('title', 'soundcloud_title',),
        ('html', 'embed',),
    )

    @property
    def oembed_resource(self):
        return self.soundcloud_url

    @property
    def oembed_endpoint_params(self):
        params = {
            'auto_play': str(self.auto_play).lower(),
            'show_comments': str(self.show_comments).lower(),
            'iframe': str(self.html5_player).lower(),
        }
        if self.maxwidth:
            params['maxwidth'] = self.maxwidth
        if self.maxheight:
            params['maxheight'] = self.maxheight
        if self.color:
            params['color'] = self.color
        return params

    def oembed_clean_value(self, key, value):
        if key == 'width' and value == '100%':
            return None
        return value
