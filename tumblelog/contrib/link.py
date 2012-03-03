from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.models import BasePostType
from tumblelog.settings import TEXTFIELD_HELP_TEXT


class Link(BasePostType):
    """
    Post type for a link.
    """
    link = models.URLField(_('URL'), verify_exists=False)
    link_text = models.CharField(_('Link Text'), max_length=256, null=True, \
        blank=True)
    caption = models.TextField(_('Caption'),
        null=True,
        blank=True,
        help_text=TEXTFIELD_HELP_TEXT
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': (
                    'title',
                    ('link', 'link_text',),
                    'caption',
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
        ]
