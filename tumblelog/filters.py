from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class PubliclyVisibleListFilter(SimpleListFilter):
    """
    A list filter that allows users to filter by the publication date
    """
    title = _('Visibility to Public')
    parameter_name = 'public'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Visible')),
            ('0', _('Not Visible')),
        )

    def queryset(self, request, queryset):
        if queryset:
            kls = queryset[0].__class__
            value = self.value()
            if value == '0':
                private = [x.id for x in kls.objects.private()]
                return queryset.filter(pk__in=private)
            elif value == '1':
                public = [x.id for x in kls.objects.public()]
                return queryset.filter(pk__in=public)


class PublicationDateListFilter(SimpleListFilter):
    """
    A list filter that allows users to filter by the publication date
    """
    title = _('Publication Date')
    parameter_name = 'pub_date'

    def lookups(self, request, model_admin):
        return (
            ('future', _('In the future')),
            ('past', _('In the past')),
        )

    def queryset(self, request, queryset):
        if queryset:
            kls = queryset[0].__class__
            value = self.value()
            if value == 'future':
                future = [x.id for x in kls.objects.queued()]
                return queryset.filter(pk__in=future)
            elif value == 'past':
                past = [x.id for x in kls.objects.past()]
                return queryset.filter(pk__in=past)


class StatusListFilter(SimpleListFilter):
    """
    A list filter that allows users to filter by the post status
    """
    title = _('Status')
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('draft', _('Draft')),
            ('published', _('Published')),
        )

    def queryset(self, request, queryset):
        if queryset:
            value = self.value()
            if value == 'draft':
                return queryset.filter(status='d')
            elif value == 'published':
                return queryset.filter(status='p')
