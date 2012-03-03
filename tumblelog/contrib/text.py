from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.models import BasePostType
from tumblelog.settings import TEXTFIELD_HELP_TEXT


class Text(BasePostType):
    """
    Post type for a small blurb of text
    """
    body = models.TextField(_('Body'), help_text=TEXTFIELD_HELP_TEXT)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = _('Text')
        verbose_name_plural = _('Text')

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'body',)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published',),
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
            'body',
        ]


class Article(BasePostType):
    """
    Post type for a blurb of text with an excerpt.
    """
    excerpt = models.TextField(_('Excerpt'), help_text=TEXTFIELD_HELP_TEXT)
    body = models.TextField(_('Body'), help_text=TEXTFIELD_HELP_TEXT)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'body', 'excerpt',)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published',),
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
            'body',
            'excerpt',
        ]
