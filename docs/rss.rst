RSS Feeds
=========

An RSS feed is automatically generated for the tumblelog. It can be included in templates by reversing the view's URL with the `{% url %} template tag <https://docs.djangoproject.com/en/dev/ref/templates/builtins#url>`_.

::

    {% load url from future %}

    <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="{% url 'tumblelog:feed' %" />

The feed may be customized via 4 settings:

- :ref:`TUMBLELOG_RSS_TITLE <tumblelog_rss_title_setting>`
- :ref:`TUMBLELOG_RSS_DESCRIPTION <tumblelog_rss_description_setting>`
- :ref:`TUMBLELOG_RSS_LINK <tumblelog_rss_link_setting>`
- :ref:`TUMBLELOG_RSS_NUM <tumblelog_rss_num_setting>`
