from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

from tumblelog.choices import STATUS_CHOICES
from tumblelog.managers import PostManager


class PostStatusMixin(models.Model):
    """
    Adds the status field + convenience methods for checking whether objects
    are published or draft.
    """
    status = models.CharField(_('Status'),
        max_length=1,
        default='d',
        choices=STATUS_CHOICES,
        help_text=_('Draft posts are not visible to the public')
    )

    class Meta:
        abstract = True

    @property
    def is_draft(self):
        "Boolean indicating whether post is marked as 'Draft'"
        return self.status == 'd'

    @property
    def is_published(self):
        "Boolean indicating whether post is marked as 'Published'"
        return self.status == 'p'


class PostDateMixin(models.Model):
    """
    Adds fields for the date that posts are added, modified, and published +
    convenience methods for checking whether objects are queued or past.
    """
    date_added = models.DateTimeField(_('Creation Date'), auto_now_add=True)
    date_modified = models.DateTimeField(_('Modification Date'), auto_now=True)
    date_published = models.DateTimeField(_('Publication Date'),
        null=True,
        blank=True,
        help_text=_((
            'By setting a publication date in the future, you can schedule '
            'posts for a future date and time.'
        ))
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.date_published:
            self.date_published = datetime.now()
        super(PostDateMixin, self).save(*args, **kwargs)

    @property
    def is_past(self):
        """
        Boolean indicating whether post is past (i.e. whether date published is
        in the past)
        """
        return self.date_published <= datetime.now()

    @property
    def is_queued(self):
        """
        Boolean indicating whether post is queued (i.e whether date published
        is in the future)
        """
        return self.date_published > datetime.now()


class PostMetaMixin(PostStatusMixin, PostDateMixin, models.Model):
    """
    For convenience, combines four unique bits of functionality that have bits
    of interdependence, but still make sense to break out into bits of related
    functionality:

    * PostStatusMixin, which adds the status field + convenience methods for
      checking whether objects are published or draft.
    * PostDateMixin, which adds fields for the date that posts are added,
      modified, and published + convenience methods for checking whether
      objects are queued or past.
    * The PostManager, which adds filtering methods for only returning queued,
      past, draft, published, and public (published + past) objects.
    * The is_public method, which ensures that objects are both published and
      published in the past.

    Intended to be used on both the Post and BasePostType models.
    """
    objects = PostManager()

    class Meta:
        abstract = True

    @property
    def is_public(self):
        """
        Boolean indicating whether post is public (i.e. marked as published and
        publish date is in the past)
        """
        return self.is_past & self.is_published
