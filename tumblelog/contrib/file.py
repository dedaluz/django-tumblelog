import re

from django.db import models
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.models import BasePostType
from tumblelog.settings import TEXTFIELD_HELP_TEXT


class File(BasePostType):
    """
    Post type for a downloadable file
    """
    file_file = models.FileField(_('File'),
        upload_to='tumblelog/file'
    )
    file_name = models.CharField(_('File Name'),
        max_length=128,
        blank=True,
        null=True,
        help_text=_('Defaults to the filename')
    )
    description = models.TextField(_('Description'),
        blank=True,
        null=True,
        help_text=TEXTFIELD_HELP_TEXT
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

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
                    ('file_file', 'file_name',),
                    'description',
                ),
            }),
            (_('Meta'), {
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
            'description',
        ]

    def get_filename(self):
        """
        Returns the filename of the uploaded file
        """
        if self.file_file:
            try:
                return re.search(r'([^\/]+)$', self.file_file).groups()[0]
            except AttributeError:
                pass
        return None

    @property
    def file_link_text(self):
        """
        Returns text to be used for a download link
        """
        if self.file_name:
            return self.file_name
        return self.get_filename()
