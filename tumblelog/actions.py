from django.utils.translation import ugettext as _


def mark_as_published(self, request, queryset):
    "Admin action to mark posts as published"
    for post in queryset:
        post.status = 'p'
        post.save()
mark_as_published.short_description = _('Mark selected posts as published')


def mark_as_draft(self, request, queryset):
    "Admin action to mark posts as draft"
    for post in queryset:
        post.status = 'd'
        post.save()
mark_as_draft.short_description = _('Mark selected posts as draft')
