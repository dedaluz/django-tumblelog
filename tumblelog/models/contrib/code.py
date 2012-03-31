import re

from django.contrib import admin
from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from tumblelog import actions, filters
from tumblelog.choices import CODE_LANGUAGES
from tumblelog.fields import OEmbedURLField
from tumblelog.models.base import BasePostType, BaseOembedRich
from tumblelog.settings import TEXTFIELD_HELP_TEXT


class CodeSnippet(models.Model):
    """
    A single code snippet, used as an inline to the Code post type
    """
    post = models.ForeignKey('tumblelog.Code')
    name = models.CharField(_('Snippet Name'), max_length=128)
    language = models.CharField(_('Language'),
        max_length=64,
        choices=CODE_LANGUAGES,
    )
    code = models.TextField(_('Code'))

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Code Snippet'
        verbose_name_plural = 'Code Snippets'

    def __unicode__(self):
        return self.name


class CodeSnippetInline(admin.StackedInline):
    model = CodeSnippet
    extra = 1


class Code(BasePostType):
    """
    Post type for a series of one or more code snippets
    """
    caption = models.TextField(_('Caption'),
        blank=True,
        null=True,
        help_text=TEXTFIELD_HELP_TEXT
    )

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Code'
        verbose_name_plural = 'Code'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'caption',)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published', 'author',)
            }),
        )
        inlines = [
            CodeSnippetInline,
        ]
        list_display = (
            'title',
            'author',
            'date_published',
            'status',
        )
        list_filter = (
            filters.PubliclyVisibleListFilter,
            filters.PublicationDateListFilter,
            filters.StatusListFilter,
            'author',
        )
        prepopulated_fields = {
            'slug': ('title',)
        }
        search_fields = [
            'title',
            'slug',
            'caption',
        ]

    @property
    def snippets(self):
        return self.codesnippet_set.all()


class Gist(BaseOembedRich):
    """
    Post type to include a code snippet from GitHub's Gist service:
    https://gist.github.com/
    """
    gist_url = OEmbedURLField(_('Gist URL'), max_length=1024)
    git_user = models.CharField(_('Author\'s Name'), max_length=512, \
        editable=False)
    git_user_url = models.URLField(_('Author\'s Twitter Profile'), \
        max_length=512, editable=False)
    gist_title = models.CharField(_('Author\'s Name'), max_length=512, \
        editable=False)

    class Meta:
        app_label = 'tumblelog'
        verbose_name = 'Gist'
        verbose_name_plural = 'Gists'

    class TumblelogMeta:
        actions = [
            actions.mark_as_published,
            actions.mark_as_draft,
        ]
        date_hierarchy = 'date_published'
        fieldsets = (
            (None, {
                'fields': ('title', 'gist_url', 'caption',)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': ('status', 'slug', 'date_published', 'author',)
            }),
        )
        list_display = (
            'title',
            'author',
            'date_published',
            'status',
        )
        list_filter = (
            filters.PubliclyVisibleListFilter,
            filters.PublicationDateListFilter,
            filters.StatusListFilter,
            'author',
        )
        prepopulated_fields = {
            'slug': ('title',)
        }
        search_fields = [
            'title',
            'slug',
            'caption',
        ]

    oembed_endpoint = 'https://github.com/api/oembed'
    oembed_schema = [
        'https://gist.github.com/*',
    ]
    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        ('url', 'gist_url',),
        ('author_url', 'git_user_url',),
        ('author_name', 'git_user',),
        ('title', 'gist_title',),
        ('html', 'embed'),
    )

    @property
    def oembed_resource(self):
        return self.gist_url

    @property
    def gist_id(self):
        """
        Returns GitHub's ID for the Gist.

        This method is necessarily fragile, as Gist's oEmbed response does not
        return this value.
        """
        return int(re.search(r'(\d+)$', self.gist_url).groups()[0])

    @property
    def javascript_embed(self):
        """
        Uses the Gist embed code (which is not what is returned by the oEmbed
        call) to display the Gist, using the naked data returned by oEmbed <aside>
        a noscript fallback.
        """
        return render_to_string('tumblelog/gist_javascript_embed.html', {
            'id': self.gist_id,
            'noscript': self.embed,
        })
