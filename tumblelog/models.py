from datetime import datetime, timedelta
import oembed
from urllib2 import HTTPError

from django.contrib.admin import helpers
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db import models
from django.utils.translation import ugettext as _

from tumblelog.contrib import CONTRIB_POST_TYPES
from tumblelog.managers import PostManager
from tumblelog.mixins import PostMetaMixin
from tumblelog.settings import POST_TYPES, OEMBED_DEFAULT_CACHE_AGE, \
    TEXTFIELD_HELP_TEXT
from tumblelog.util import path_break


class TumblelogMeta(object):
    """
    A special Meta class for BasePostType subclasses; all properties defined
    herein are ultimately added to BasePostType._tumblelog_meta
    """
    raw_id_fields = None
    fields = None
    exclude = None
    fieldsets = None
    form = None
    filter_vertical = None
    filter_horizontal = None
    radio_fields = None
    prepopulated_fields = None
    formfield_overrides = None
    readonly_fields = None
    ordering = None
    list_display = None
    list_display_links = None
    list_filter = None
    list_select_related = None
    list_per_page = None
    list_max_show_all = None
    list_editable = None
    search_fields = None
    date_hierarchy = None
    save_as = None
    save_on_top = None
    paginator = None
    inlines = None
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_on_top = False
    paginator = Paginator
    inlines = []
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    actions = []
    action_form = helpers.ActionForm
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

    def __init__(self, opts, **kwargs):
        if opts:
            opts = opts.__dict__.items()
        else:
            opts = []
        opts.extend(kwargs.items())

        for key, value in opts:
            setattr(self, key, value)

    def __iter__(self):
        return iter([(k, v) for (k, v) in self.__dict__.items()])


class Post(PostMetaMixin, models.Model):
    """
    A generic post model, consisting of a single generic foreign key and a set
    of fields commonly used to look up posts. This is intended to be used to
    create aggregate querysets of all subclasses of BasePostType.
    """
    post_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    fields = generic.GenericForeignKey('post_type', 'object_id')
    slug = models.SlugField(_('Slug'),
        max_length=64,
        help_text=_('Used to construct the post\'s URL')
    )

    objects = PostManager()

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return '%s (%s)' % (self.fields.title, self.fields.__class__.__name__,)

    @models.permalink
    def get_absolute_url(self):
        return ('tumblelog:detail', [], {'slug': self.fields.slug})


class PostTypeMetaclass(models.base.ModelBase):
    """
    Metaclass for BasePostType models.
    """
    def __new__(cls, name, bases, attrs):
        """
        Creates a TumblelogMeta instance, accessible as obj._tumblelog_meta in
        any BasePostType subclasses.
        """
        opts = TumblelogMeta(attrs.pop('TumblelogMeta', None))
        attrs['_tumblelog_meta'] = opts

        # Make public pointer for templating
        def get_tumblelog_meta(self):
            return self._tumblelog_meta
        attrs['tumblelog_meta'] = get_tumblelog_meta

        return super(PostTypeMetaclass, cls).__new__(cls, name, bases, attrs)


class BasePostType(PostMetaMixin, models.Model):
    """
    Abstract base class whose subclasses carry the constituent fields of each
    post type.
    """
    title = models.CharField(_('Title'), max_length=256)
    slug = models.SlugField(_('Slug'),
        max_length=64,
        help_text=_('Used to construct the post\'s URL')
    )
    post = generic.GenericRelation(Post, content_type_field='post_type', \
        object_id_field='object_id')

    __metaclass__ = PostTypeMetaclass

    class Meta:
        abstract = True
        ordering = ['-date_published']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.post.all()[0].get_absolute_url()

    def save(self, *args, **kwargs):
        """
        Overrides save method to either creates or updates the correspondant
        Post object when object is saved.
        """
        super(BasePostType, self).save(*args, **kwargs)
        content_type = ContentType.objects.get_for_model(self)
        post, created = Post.objects.get_or_create(
            post_type=content_type,
            object_id=self.id
        )
        post.status = self.status
        post.date_added = self.date_added
        post.date_modified = self.date_modified
        post.date_published = self.date_published
        post.slug = self.slug
        post.save()


class BaseOembedPostType(BasePostType):
    """
    Abstract post type base classes whose subclasses retrieve data from an
    oEmbed endpoint.
    """
    caption = models.TextField(_('Caption'),
        blank=True,
        null=True,
        help_text=TEXTFIELD_HELP_TEXT
    )
    version = models.CharField(_('oEmbed Version'), max_length=3, null=True, \
        blank=True, editable=True)
    provider_name = models.CharField(_('oEmbed Provider Name'), \
        max_length=128, blank=True, null=True, editable=True)
    provider_url = models.CharField(_('oEmbed Provider URL'), max_length=512, \
        blank=True, null=True, editable=True)
    cache_age = models.IntegerField(_('Cache Age'), \
        default=OEMBED_DEFAULT_CACHE_AGE)
    date_updated = models.DateTimeField(_('Last Retrieved'), null=True, \
        blank=True, editable=True)

    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
    )
    oembed_endpoint = None
    oembed_schema = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(BaseOembedPostType, self).__init__(*args, **kwargs)
        if self.pk:
            expiry = timedelta(seconds=self.cache_age) + self.date_updated
            if datetime.now() > expiry:
                self.oembed_update()

    def oembed_consumer(self):
        consumer = oembed.OEmbedConsumer()
        endpoint = oembed.OEmbedEndpoint(
            self.oembed_endpoint,
            self.oembed_schema,
        )
        consumer.addEndpoint(endpoint)
        return consumer

    @property
    def oembed_resource(self):
        return None

    @property
    def oembed_endpoint_params(self):
        return {}

    def oembed_update(self):
        self.date_updated = datetime.now()
        response = self.oembed_retrieve()
        self.oembed_map_values(response)

    def oembed_retrieve(self, suppress_http_errors=True):
        consumer = self.oembed_consumer()
        try:
            return consumer.embed(self.oembed_resource, 'json', \
                **self.oembed_endpoint_params)
        except HTTPError, e:
            if not suppress_http_errors:
                raise e

    def oembed_map_values(self, response):
        for mapping in self.oembed_map:
            try:
                prop, field = mapping
            except ValueError:
                prop, field = mapping, mapping
            finally:
                if hasattr(self, field):
                    value = self.oembed_clean_value(field, response[prop])
                    setattr(self, field, value)

    def oembed_clean_value(self, key, value):
        return value

    def save(self, *args, **kwargs):
        self.oembed_update()
        super(BaseOembedPostType, self).save(*args, **kwargs)


class BaseOembedPhoto(BaseOembedPostType):
    width = models.IntegerField(_('Width'), blank=True, null=True, \
        editable=False)
    height = models.IntegerField(_('Height'), blank=True, null=True, \
        editable=False)
    image_url = models.URLField(_('Image URL'), blank=True, null=True, \
        editable=False)

    class Meta:
        abstract = True

    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('url', 'image_url',)
    )


class BaseOembedVideo(BaseOembedPostType):
    width = models.IntegerField(_('Width'), blank=True, null=True, \
        editable=False)
    height = models.IntegerField(_('Height'), blank=True, null=True, \
        editable=False)
    embed = models.TextField(_('Embed Code'), blank=True, null=True, \
        editable=False)

    class Meta:
        abstract = True

    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('html', 'embed',),
    )


class BaseOembedLink(BaseOembedPostType):
    """

    """
    class Meta:
        abstract = True


class BaseOembedRich(BaseOembedPostType):
    width = models.IntegerField(_('Width'), blank=True, null=True, \
        editable=False)
    height = models.IntegerField(_('Height'), blank=True, null=True, \
        editable=False)
    embed = models.URLField(_('Embed Code'), blank=True, null=True, \
        editable=False)

    class Meta:
        abstract = True

    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'width',
        'height',
        ('html', 'embed',)
    )


"""
Parse through the list of all CONTRIB_POST_TYPES and other post types defined
in TUMBLELOG_POST_TYPES, adding any not already defined in this module to
locals(). This allows Django to discover them and manage their database tables
as appropriate.
"""
for post_type in CONTRIB_POST_TYPES + POST_TYPES:
    path, model = path_break(post_type)
    if not model in locals():
        module = __import__(path, globals(), locals(), [model], -1)
        locals()[model] = getattr(module, model)  # Ew.
