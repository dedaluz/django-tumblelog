django-tumblelog
================

Jason Kottke `defined <http://www.kottke.org/05/10/tumblelogs/>`_ tumblelogs as:

    a quick and dirty stream of consciousness, a bit like a remaindered links style linklog but with more than just links [...] really just a way to quickly publish the "stuff" that you run across every day on the web. [They have] different ways of displaying various types of content...remaindered links, regular posts, book reviews, and movie reviews are all displayed differently.

Perhaps the best implementation of this model is `Tumblr <http://tumblr.com>`_, a simple hosted tumblelog service that allows you to post text snippets, photos, quotes, links, chat logs, audio files, or video files. While an excellent service, it is a bit limiting; post formats are restricted to those seven things. If you would like a standard format to your recipes or code snippets, you're out of luck. 

``django-tumblelog`` is an attempt to provide more flexibility to this format by giving you full control over each post type.

Features
--------

* Simple definition of custom post types
* Large stable of contrib post types to get started quickly.

  - Post short text blurbs, long-form articles, links, files, and photos.

* oEmbed support, for embedding of 3rd-party media in posts.

  - Post directly from Twitter, Flickr, Instagram, Rdio, SoundCloud, Vimeo, YouTube, and GitHub.

* Optional integration with `django-taggit <http://django-taggit.readthedocs.org/>`_
* Takes full advantage of Django's templating system
* Agnostic of commenting system and markup format.
* Internationalization-ready
* Post scheduling
* Draft posts
* Multi-author support with object-level permissions
* RSS feed

User Guide
----------

Installing and using tumblelog:

.. toctree::
   :maxdepth: 2

   installation
   posts
   templating
   rss
   configuration
   contrib
   oembed