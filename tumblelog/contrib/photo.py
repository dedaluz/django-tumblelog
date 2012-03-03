from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.choices import FLICKR_SIZE_CHOICES
from tumblelog.fields import OEmbedURLField
from tumblelog.models import BasePostType, BaseOembedPhoto
from tumblelog.settings import FLICKR_WIDTH, TEXTFIELD_HELP_TEXT


class Image(BasePostType):
    """
    Post type for an image.
    """
    image = models.ImageField(_('Image'), upload_to='tumblelog/image')
    caption = models.TextField(_('Caption'),
        blank=True,
        null=True,
        help_text=TEXTFIELD_HELP_TEXT
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'image', 'caption',)
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
        ]


class Flickr(BaseOembedPhoto):
    """
    Post type for an image from Flickr, with metadata pulled directly from the
    source using Flickr's oEmbed API.
    """
    flickr_url = OEmbedURLField(_('Flickr URL'),
        max_length=1024
    )
    flickr_user = models.CharField(_('Photographer\'s Name'),
        max_length=512,
        editable=False
    )
    flickr_user_url = models.URLField(_('Photographer\'s Flickr Stream'),
        null=True,
        blank=True,
        max_length=1024,
        editable=False
    )
    flickr_title = models.CharField(_('Flickr Title'),
        max_length=512,
        editable=False
    )
    size = models.CharField(_('Size'),
        max_length=4,
        default=FLICKR_WIDTH,
        choices=FLICKR_SIZE_CHOICES
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Flickr Photo'
        verbose_name_plural = 'Flickr Photos'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        change_form_template = 'admin/flickr_change_form.html'
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'flickr_url', 'size', 'caption',)
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

    oembed_endpoint = 'http://www.flickr.com/services/oembed'
    oembed_schema = [
        'http://www.flickr.com/photos/*',
        'http://flic.kr/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('url', 'image_url',),
        ('author_name', 'flickr_user',),
        ('author_url', 'flickr_user_url',),
        ('title', 'flickr_title',),
    )

    @property
    def oembed_resource(self):
        return self.flickr_url

    @property
    def oembed_endpoint_params(self):
        return {
            'maxwidth': self.size,
            'maxheight': self.size,
        }


class Instagram(BaseOembedPhoto):
    """
    Post type for an image from Instagram, with metadata pulled directly from
    the source using Instagram's oEmbed API.
    """
    instagram_url = OEmbedURLField(_('Instagram URL'), max_length=1024)
    instagram_user = models.CharField(_('Photographer\'s Name'),
        max_length=512,
        editable=False,
    )
    instagram_title = models.CharField(_('Instagram Title'),
        max_length=512,
        editable=False,
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Instagram Photo'
        verbose_name_plural = 'Instagram Photos'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        change_form_template = 'admin/instagram_change_form.html'
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'instagram_url', 'caption',)
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
        ]

    oembed_endpoint = 'http://api.instagram.com/oembed'
    oembed_schema = [
        'http://instagr.am/p/*',
        'http://instagram.com/p/*/',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('url', 'image_url',),
        ('author_name', 'instagram_user',),
        ('title', 'instagram_title',),
    )

    @property
    def oembed_resource(self):
        return self.instagram_url
