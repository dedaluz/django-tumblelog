from copy import deepcopy

from django.contrib import admin

from tumblelog.settings import POST_TYPES
from tumblelog.util import import_model


class PostTypeAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        """
        Hook for specifying fieldsets for the add form, modified to only
        display fields inside fieldsets that the user has permission to change.
        """
        if self.declared_fieldsets:
            fieldsets = self.declared_fieldsets
        else:
            form = self.get_form(request, obj)
            fieldsets = form.base_fields.keys() + \
                list(self.get_readonly_fields(request, obj))
        fieldsets = super(PostTypeAdmin, self).get_fieldsets(request, obj=obj)
        fieldsets = deepcopy(fieldsets)
        for fieldset in fieldsets:
            fieldset[1]['fields'] = [field for field in fieldset[1]['fields'] \
                if self.can_change_field(request, obj, field)]
        for fieldset in fieldsets:
            if not fieldset[1]['fields']:
                fieldsets.remove(fieldset)

        return fieldsets

    def get_form(self, request, obj=None):
        """
        Returns a Form class (used by add_view and change_view) modified to
        only include fields the user has permissions to view.
        """
        form = super(PostTypeAdmin, self).get_form(request, obj)
        for field_name, field in form.base_fields.items():
            if not self.can_change_field(request, obj, field_name):
                del form.base_fields[field_name]
        return form

    def can_change_field(self, request, obj, field_name):
        """
        Returns boolean indicating whether the user has necessary permissions to
        view the passed field.
        """
        return True


# Dynamically generate admin class from values passed to TumblelogMeta
for post_type in POST_TYPES:
    model = import_model(post_type)
    admin_cls = type(
        PostTypeAdmin.__name__,
        (PostTypeAdmin,),
        dict((k, v,) for k, v in model._tumblelog_meta if not k.startswith('_'))
    )
    admin.site.register(model, admin_cls)
