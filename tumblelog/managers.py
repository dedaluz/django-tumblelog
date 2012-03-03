from datetime import datetime

from django.db import models
from django.db.models import Q


class PostManager(models.Manager):
    """
    Custom model manager for Post and BasePostType. Adds filtering methods for
    only returning queued, past, draft, published, private, and public
    (published + past) objects.
    """

    def queued(self):
        "Returns queued posts (i.e. publish date is in the future)"
        return self.get_query_set().filter(date_published__gt=datetime.now())

    def past(self):
        "Returns past posts (i.e. publish date is in the past)"
        return self.get_query_set().filter(date_published__lte=datetime.now())

    def status(self, status_code):
        "Convenience method for filtering objects by the status field."
        return self.get_query_set().filter(status=status_code)

    def draft(self):
        "Returns posts marked as 'Draft'"
        return self.status('d')

    def published(self):
        "Returns posts marked as 'Published'"
        return self.status('p')

    def private(self):
        "Returns private posts (i.e. either future or draft)"
        return self.get_query_set().filter(
            Q(date_published__gt=datetime.now()) | Q(status='d')
        )

    def public(self):
        "Returns public posts (i.e. those both past and published)"
        return self.published() & self.past()
