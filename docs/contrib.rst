==================
Contrib Post Types
==================

tumblelog's ``contrib`` module provides a number of ready-made post types.

-------
Article
-------

A post type representing a long-form text post

Location:
  ``tumblelog.contrib.text.Article``

Extends:
  :ref:`BasePostType <baseposttype_class>`

Fields
------

- ``body`` - the full text of the article
- ``excerpt`` - a short excerpt of the ``body``, intended to be used in post listing views

.. _flickr_post_type:

------
Flickr
------

An `oEmbed post type </oembed>` for the `Flickr <http://flickr.com>`_ image hosting service.

Location:
  ``tumblelog.contrib.photo.Flickr``

Extends:
  :ref:`BaseOembedPhoto <oembed_photo_class>`

Fields
------

- ``flickr_url`` - the URL of the Flickr photo

Properties
----------

- ``flickr_title`` - Flickr's title for the image
- ``flickr_user`` - The Flickr uploader's username
- ``flickr_user_url`` - The URL to the Flickr uploader's photostream
- ``image_url`` - URL of the image
- ``width`` - width of the image located at ``image_url``
- ``height`` - height of the image located at ``image_url``

Settings
--------

- :ref:`TUMBLELOG_FLICKR_WIDTH <tumblelog_flickr_width_setting>`

----
File
----

A post type for a downloadable file.

Location:
  ``tumblelog.contrib.code.File``

Extends:
  :ref:`BasePostType <baseposttype_class>`

Fields
------

- ``file_file`` - the uploaded file
- ``file_name`` - a descriptive name of the file
- ``description`` - a longer description of the file

Properties
----------

- ``file_link_text`` - returns the value of the ``file_name`` field if specified; otherwise returns the filename.

----
Gist
----

An `oEmbed post type </oembed>` for GitHub's `Gist <https://gist.github.com/>`_ code snippet service.

Location:
  ``tumblelog.contrib.code.Gist``

Extends:
  :ref:`BaseOembedRich <oembed_rich_class>`

Fields
------

- ``gist_url`` - the URL of the Gist to embed

Properties
----------

- ``gist_title`` - Gist's title for snippet
- ``embed`` - the snippet's plain HTML embed code
- ``git_user`` - the author's GitHub username
- ``git_user_url`` - the URL to the author's GitHub profile
- ``gist_id`` - GitHub's ID for the Gist
- ``javascript_embed`` - embed code for Gist's more robust JavaScript embed, using the plain HTML embed code returned by oEmbed as a ``<noscript>`` fallback.

-----
Image
-----

A post type for an image file.

Location:
  ``tumblelog.contrib.photo.Image``

Extends:
  :ref:`BasePostType <baseposttype_class>`

Fields
------

- ``image`` - the uploaded image
- ``caption`` - a longer caption of the image

Properties
----------

- ``file_link_text`` - returns the value of the ``file_name`` field if specified; otherwise returns the filename.

---------
Instagram
---------

An `oEmbed post type </oembed>` for the `Instagram <http://instagr.am>`_ image sharing service.

Location:
  ``tumblelog.contrib.photo.Instagram``

Extends:
  :ref:`BaseOembedPhoto <oembed_photo_class>`

Fields
------

- ``instagram_url`` - the URL of the Instagram photo

Properties
----------

- ``instagram_title`` - Instagram's title for the image
- ``instagram_user`` - The Instagram uploader's username
- ``image_url`` - URL of the image
- ``width`` - width of the image located at ``image_url``
- ``height`` - height of the image located at ``image_url``

----
Link
----

A post type for a link to an external site.

Location:
  ``tumblelog.contrib.link.Link``

Extends:
  :ref:`BasePostType <baseposttype_class>`

Fields
------

- ``link`` - a URL to an external site
- ``link_text`` - text used by the link
- ``caption`` - a longer caption describing the link

----
Rdio
----

An `oEmbed post type </oembed>` for the `Rdio <http://rdio.com>`_ streaming music service. Can be used to embed an album, track, or playlist.

Location:
  ``tumblelog.contrib.audio.Rdio``

Extends:
  :ref:`BaseOembedRich <oembed_rich_class>`

Fields
------

- ``rdio_url`` - the URL of the Rdio resource

Properties
----------

- ``rdio_title`` - Rdio's title for the resource
- ``embed`` - the resource's embed code
- ``width`` - the width of the embed
- ``height`` - the height of the embed
- ``thumbnail.url`` - the URL of a thumbnail image
- ``thumbnail.width`` - an integer indicating the width of the thumbnail image
- ``thumbnail.height`` - an integer indicating the height of the thumbnail image

.. _soundcloud_post_type:

----------
SoundCloud
----------

An `oEmbed post type </oembed>` for the `SoundCloud <http://rdio.com>`_ audio sharing service. Can be used to embed a track, set, group, or user.

Location:
  ``tumblelog.contrib.audio.SoundCloud``

Extends:
  :ref:`BaseOembedRich <oembed_rich_class>`

Fields
------

- ``soundcloud_url`` - the URL of the Rdio resource
- ``maxwidth`` - the maximum allowable width for embeds
- ``maxheight`` - for SoundCloud tracks, defines the height of the returned player.
- ``color`` - a hex triplet used as an accent color in the SoundCloud embed
- ``auto_play`` - a boolean indicating whether the embed should automatically play on load
- ``show_comments`` - a boolean indicating whether SoundCloud's timed comments should be included in the embed
- ``html5_player`` - a boolean indicating whether SoundCloud's HTML5 player should be used by the embed

Properties
----------

- ``soundcloud_title`` - SoundCloud's title for the resource
- ``soundcloud_description`` - SoundCloud's description of the resource
- ``embed`` - the resource's embed code
- ``width`` - the width of the embed
- ``height`` - the height of the embed

Settings
--------

- :ref:`TUMBLELOG_SOUNDCLOUD_COLOR <tumblelog_soundcloud_color_setting>`


.. _twitter_post_type:

----
Text
----

A post type representing a short text post

Location:
  ``tumblelog.contrib.text.Text``

Extends:
  :ref:`BasePostType <baseposttype_class>`

Fields
------

- ``body`` - the full text of the post

-----
Tweet
-----

An `oEmbed post type </oembed>` for a tweet on `Twitter <https://twitter.com/>`_.

Location:
  ``tumblelog.contrib.twitter.Tweet``

Extends:
  :ref:`BaseOembedRich <oembed_rich_class>`

Fields
------

- ``tweet_url`` - the URL of the Tweet to embed
- ``hide_media`` - a boolean indicating whether the embed should include any media included in the tweet
- ``hide_thread`` - a boolean indicating whether the embed should include other tweets in the conversation
- ``maxwidth`` - the width of the of the embedded tweet, between 250 and 550 pixels
- ``language`` - a string indicating the ISO 639-1 code of language that should be used by the embed

Properties
----------

- ``width`` - the width of the embedded tweet
- ``embed`` - the tweet's embed code
- ``twitter_user`` - the author's name
- ``twitter_username`` - the author's Twitter username
- ``twitter_user_url`` - the URL to the author's Twitter stream

Settings
--------

- :ref:`TUMBLELOG_TWITTER_LANGUAGE <tumblelog_twitter_language_setting>`
- :ref:`TUMBLELOG_TWITTER_WIDTH <tumblelog_twitter_width_setting>`

-----
Vimeo
-----

An `oEmbed post type </oembed>` for the `Vimeo <http://vimeo.com/>`_ video hosting service.

Location:
  ``tumblelog.contrib.video.Vimeo``

Extends:
  :ref:`BaseOembedVideo <oembed_video_class>`

Fields
------

- ``vimeo_url`` - the URL of the video to embed

Properties
----------

- ``vimeo_title`` - Vimeo's title for snippet
- ``embed`` - the video's embed code
- ``vimeo_user`` - the author's Vimeo username
- ``vimeo_user_url`` - the URL to the author's Vimeo profile
- ``vimeo_video_id`` - Vimeo's ID for the video
- ``duration`` - the length of the embedded video, in seconds
- ``thumbnail.url`` - the URL of a thumbnail image
- ``thumbnail.width`` - an integer indicating the width of the thumbnail image
- ``thumbnail.height`` - an integer indicating the height of the thumbnail image

-------
YouTube
-------

An `oEmbed post type </oembed>` for the `YouTube <http://youtube.com/>`_ video hosting service.

Location:
  ``tumblelog.contrib.video.YouTube``

Extends:
  :ref:`BaseOembedVideo <oembed_video_class>`

Fields
------

- ``youtube_url`` - the URL of the video to embed

Properties
----------

- ``youtube_title`` - YouTube's title for snippet
- ``embed`` - the video's embed code
- ``youtube_user`` - the author's YouTube username
- ``youtube_user_url`` - the URL to the author's YouTube profile
- ``thumbnail.url`` - the URL of a thumbnail image
- ``thumbnail.width`` - an integer indicating the width of the thumbnail image
- ``thumbnail.height`` - an integer indicating the height of the thumbnail image
