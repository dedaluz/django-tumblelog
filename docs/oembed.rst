==============
oEmbed Support
==============

tumblelog provides special subclasses of :ref:`BasePostType <baseposttype_class>` which add methods and properties that facilitate retrieval and storage of data from an `oEmbed <http://oembed.com>`_ provider.

------------
How It Works
------------

oEmbed providers conform to `an API standard <http://oembed.com>`_ that reports embedding information and metadata for a specific resource (photo, video, etc) on their server.

For example, when YouTube's oEmbed endpoint is queried about `a video <http://youtu.be/dQw4w9WgXcQ>`_, it will `return <http://www.youtube.com/oembed?url=http%3A%2F%2Fyoutu.be%2FdQw4w9WgXcQ&format=json>`_ that video's embed code, dimensions, title, information about the uploader, and a thumbnail image.

tumblelog's oEmbed post types have a single editable field, denoting a resource's URL. When an instantiation is saved, the specified oEmbed provider is queried and that resource's embed code and metadata are saved in uneditable fields.

-------
Example
-------

Let's look at an example oEmbed post type that will retrieve and store information about a document on Scribd:

::

    from django.db import models

    from tumblelog.fields import OEmbedURLField
    from tumblelog.models import BaseOembedRich


    class Scribd(BaseOembedRich):
        """
        Post type for an a Scribd document, with metadata and embed code pulled
        directly from the source using Scribd's oEmbed API
        """
        scribd_url = OEmbedURLField(_('Scribd URL'), max_length=1024)

        scribd_user = models.CharField(_('Uploader\'s Username'),max_length=512,
            null=True, blank=True, editable=False)
        scribd_user_url = models.URLField(_('Uploader\'s Scribd Profile'),
            max_length=1024, null=True, blank=True, editable=False)
        scribd_title = models.CharField(_('Vimeo Title'), max_length=512,
            null=True, blank=True, editable=False)
        thumbnail_url = models.URLField(_('Thumbnail'), max_length=1024,
            null=True, blank=True, editable=False)
        thumbnail_width = models.IntegerField(_('Thumbnail Width'), null=True,
            blank=True, editable=False)
        thumbnail_height = models.IntegerField(_('Thumbnail Height'), null=True,
            blank=True, editable=False)

        class TumblelogMeta:
            prepopulated_fields = {
                'slug': ('title',)
            }

        oembed_endpoint = 'http://www.scribd.com/services/oembed'
        oembed_schema = [
            'http://www.scribd.com/doc/*',
        ]
        oembed_map = (
            'version',
            'provider_name',
            'provider_url',
            'cache_age',
            ('author_name', 'scribd_user',),
            ('author_url', 'scribd_user_url',),
            ('title', 'scribd_title',),
            ('video_id', 'vimeo_video_id',),
            ('html', 'embed',),
            'thumbnail_url',
            'thumbnail_width',
            'thumbnail_height',
        )

        @property
        def oembed_resource(self):
            return self.scribd_url

The only editable field on this model is ``scribd_url``. All other fields are uneditable, and are populated with information from the provider's response. The ``oembed_endpoint``, ``oembed_schema``, ``oembed_map``, and ``oembed_resource`` properties define this interaction and are :ref:`described in greater depth <oembed_properties>` later.

.. _oembed_type_classes:

------------
oEmbed Types
------------

The oEmbed specification defines four broad types of resource, each with their own requirements in the provider response: photo, video, link, and image. To account for those fields, there are four subclasses of ``BaseOembedPostType`` to match each type. Custom oEmbed post types should never directly inherit from ``BaseOembedPostType``; instead it should inherit from one of the following base classes, depending on the nature of the response. Each of these are defined in the ``tumblelog.models`` module.

.. _oembed_photo_class:

``BaseOembedPhoto``
-------------------

Extends ``BaseOembedPostType`` by adding three fields specific for the static photos it represents:

- ``image_url`` - URL of the image resource
- ``width`` - height of the image resource
- ``height`` - width of the image resource

.. _oembed_video_class:

``BaseOembedVideo``
-------------------

Extends ``BaseOembedPostType`` by adding three fields specific for the playable videos it represents:

- ``embed`` - video embed code
- ``width`` - width of the embedded video
- ``height`` - height of the embedded video

.. _oembed_link_class:

``BaseOembedLink``
------------------

Subclasses but does not extend ``BaseOembedPostType``, as there are no additional fields required by the oembed specifications.

.. _oembed_rich_class:

``BaseOembedRich``
------------------

Extends ``BaseOembedPostType`` by adding three fields specific for the rich media it represents:

- ``embed`` - embed code
- ``width`` - width of the embed
- ``height`` - height of the embedd

.. _oembed_properties:

----------
Properties
----------

Each oEmbed post type should define each of these properties.

``oembed_resource``
-------------------

A model method decorated with ``@property`` indicating the URL of the resource. Typically this will server as a pointer to a field on the model, as demonstrated in the example:

::

    @property
    def oembed_resource(self):
        return self.scribd_url

The field referenced should always be an ``OEmbedURLField``.

``oembed_endpoint``
-------------------

A string indicating the URL of the provider's oEmbed endpoint.

::

    oembed_endpoint = 'http://www.scribd.com/services/oembed'

``oembed_schema``
-----------------

A list of `glob <http://en.wikipedia.org/wiki/Glob_(programming)>`_-style patterns indicating valid resource patterns. On Scribd, there is only one valid pattern; others may have more. When developing custom oEmbed post types, consider short URL patterns and multiple resource types while defining this property.

If the value specified by ``oembed_resource`` does not match any of these patterns, a validation error is raised.

::

    oembed_schema = [
        'http://www.scribd.com/doc/*',
    ]

``oembed_map``
--------------

A tuple mapping properties of the provider response to fields on the post type's model. If a member of the tuple is a string, then it is mapped to a field

::

    oembed_map = (
        'version',
        'provider_name',
        'provider_url',
        'cache_age',
        ('author_name', 'scribd_user',),
        ('author_url', 'scribd_user_url',),
        ('title', 'scribd_title',),
        ('video_id', 'vimeo_video_id',),
        ('html', 'embed',),
        'thumbnail_url',
        'thumbnail_width',
        'thumbnail_height',
    )

In this example, the ``thumbnail_url`` value from the provider response is stored on the ``thumbnail_url`` field on the Scribd model. The ``author_name`` value from the response is stored on the ``scribd_user`` field.

------
Fields
------

These fields are added by the ``BaseOembedPostType`` model.

- ``caption`` - a text field serving as a caption for the resource
- ``version`` - the oEmbed version specified in the provider response. Currently always "1.0"
- ``provider_name`` - the name of of oEmbed provider, specified in the provider response
- ``provider_url`` - the url of of oEmbed provider, specified in the provider response
- ``date_updated`` - the time and date of the most recent fetch of data.
- ``cache_age`` - the number of seconds to cache the provider response. tumblelog will honor this, attempting to refetch the data after this number of seconds has elapsed since ``date_updated``. This defaults to the value specified in ``OEMBED_DEFAULT_CACHE_AGE``.

Other fields may be added by the :ref:`specific oEmbed type <oembed_type_classes>` being used.
