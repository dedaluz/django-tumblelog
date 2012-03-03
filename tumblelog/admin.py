from django.contrib import admin

from tumblelog.settings import POST_TYPES
from tumblelog.util import import_from


class PostTypeAdmin(admin.ModelAdmin):
    pass


# Dynamically generate admin class from values passed to TumblelogMeta
for post_type in POST_TYPES:
    model = import_from(post_type)
    admin_cls = type(
        PostTypeAdmin.__name__,
        (PostTypeAdmin,),
        dict((k, v,) for k, v in model._tumblelog_meta if not k.startswith('_'))
    )
    admin.site.register(model, admin_cls)
