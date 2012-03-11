Configuration
=============

tumblelog may be configured with the following settings


.. _tumblelog_post_types_setting:

TUMBLELOG_POST_TYPES
--------------------

Optional, but recommended; a list of :ref:`post types <baseposttype_class>` you'd like to use. These should take the form of ``'app.Model'``, rather than being full import paths. 

Default:
::

    [
        'tumblelog.Article',
        'tumblelog.Text',
        'tumblelog.File',
        'tumblelog.Image',
    ]

Example:

::

    TUMBLELOG_POST_TYPES = [
        'tumblelog.Text',
        'tumblelog.Image',
        'recipes.Recipe',
    ]


TUMBLELOG_TEXTFIELD_HELP_TEXT
-----------------------------

Optional; a string used for ``help_text`` for each ``TextField`` in the `contrib post types </contrib>`.

Default: ``''``

::

    TUMBLELOG_TEXTFIELD_HELP_TEXT = 'Uses Markdown'

TUMBLELOG_OEMBED_DEFAULT_CACHE_AGE
----------------------------------

Optional; an integer indicating the number of seconds tumblelog should cache oEmbed provider responses.

Default: ``86400`` (1 day)

::
    
    TUMBLELOG_OEMBED_DEFAULT_CACHE_AGE = 60 * 60 * 24 * 7  # 1 week

.. _tumblelog_flickr_width_setting:

TUMBLELOG_FLICKR_WIDTH
----------------------

Optional; an integer indicating the default width of images retrieved using the :ref:`Flickr post type <flickr_post_type>`. Must be one of '640', '500', '240', '100', or '75'.

Default: ``640``

::

    TUMBLELOG_OEMBED_DEFAULT_CACHE_AGE = 75

.. _tumblelog_twitter_language_setting:

TUMBLELOG_TWITTER_LANGUAGE
--------------------------

Optional; a string indicating the ISO 639-1 code of the default language of Tweets retrieved using the :ref:`Twitter post type <twitter_post_type>`. Currently supported:

- ``zh-cn``: Chinese (Simplified)
- ``zh-tw``: Chinese (Traditional)
- ``da``: Danish
- ``nl``: Dutch
- ``en``: English
- ``fi``: Filipino
- ``fi``: Finnish
- ``fr``: French
- ``de``: German
- ``hi``: Hindi
- ``id``: Indonesian
- ``it``: Italian
- ``ja``: Japanese
- ``ko``: Korean
- ``ms``: Malay
- ``no``: Norwegian
- ``pl``: Polish
- ``pt``: Portuguese
- ``ru``: Russian
- ``es``: Spanish
- ``sv``: Swedish
- ``tr``: Turkish

Default: ``'en'``

::

    TUMBLELOG_TWITTER_LANGUAGE = 'ms'

.. _tumblelog_twitter_width_setting:

TUMBLELOG_TWITTER_WIDTH
-----------------------

Optional; an integer indicating the default width of tweets embedded using the :ref:`Twitter post type <twitter_post_type>`.

Default: ``325``

::

    TUMBLELOG_TWITTER_WIDTH = 500

.. _tumblelog_soundcloud_color_setting:

TUMBLELOG_SOUNDCLOUD_COLOR
--------------------------

Optional; a string containing a hex triplet used as an accent color with the SoundCloud embed, when using the :ref:`SoundCloud post type <soundcloud_post_type>`.

Default: ``''``

::

    TUMBLELOG_SOUNDCLOUD_COLOR = 'FF00FF'
