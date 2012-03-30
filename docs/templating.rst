==========
Templating
==========

tumblelog comes with a set of basic templates that should be used as a basis for you to build your own.

--------------
Global Context
--------------

In all tumblelog views, the following context variables are always available:

- ``{{ list_view }}`` - A boolean representing whether the current view is a list of posts
- ``{{ detail_view }}`` - A boolean representing whether the current view is the detail of a single post

---------------
Basic Templates
---------------

The following templates are used aspecifically to post types.

.. _post_list_template:

tumblelog/post_list.html
========================

This template is used to display a list of :ref:`Post <post_class>` objects.

Context
-------

- ``{{ posts }}`` - A queryset of :ref:`Post <post_class>` objects.

Example
-------

::

    {% load i18n %}

    {% if posts %}
        {% for post in posts %}
            {% include 'tumblelog/post.html' %}
        {% endfor %}
    {% else %}
        {% blocktrans %}
            <p>There are no public posts. Get writing! This blog won't author itself. That functionality is coming in v2.0.</p>
        {% endblocktrans %}
    {% endif %}

    {% include 'tumblelog/pagination.html' %}

.. _post_detail_template:

tumblelog/post_detail.html
==========================

This template is used in a single :ref:`Post <post_class>` object's detail view.

Context
-------

- ``{{ post }}`` - A single ``Post`` object. See the :ref:`Post class documentation <post_class>` for more details on its fields and properties.

Example
-------

::

    {% block main %}
        {% include "tumblelog/post.html" %}
    {% endblock main %}

tumblelog/post.html
===================

This template is intended to be used any time a :ref:`Post <post_class>` object is displayed. It should be used as an include in both the :ref:`post_list.html <post_list_template>` and :ref:`post_detail.html <post_detail_template>` templates.

Context
-------

- ``{{ post }}`` - A single ``Post`` object. See the :ref:`Post class documentation <post_class>` for more details on its fields and properties.

Example
-------

::

    <article class="{{ post.post_type_name }}">
         <header>
             <h2><a href="{{ post.get_absolute_url }}">{{ post.fields.title }}</a></h2>
             <time pubdate="pubdate" datetime="{{ post.date_published|date:"m-d-Y" }}">{{ post.date_published|date:"F j, Y" }}</time>
         </header>
         {% include post.fields.post_template %}
    </article>

.. _post_type_templates:

-------------------
Post Type Templates
-------------------

As each post type has a unique schema and intended usage, each one requires its own set of templates. The name of each template is derived from a slugified version of its class name, using Django's `slugify <https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#slugify>`_ function.

.. _post_type_post_template:

tumblelog/post/<post_type>.html
===============================

This template is used to display the body of posts of this type.

Context
-------

- ``{{ post }}`` - A single ``Post`` object. See the :ref:`Post class documentation <post_class>` for more details on its fields and properties.

Example
-------

This example is from the :ref:`article post type <article_post_type>`, located at ``tumblelog/post/article.html``.

::

    {% load i18n %}

    {% if detail_view %}
         {{ post.fields.body|linebreaks }}
    {% endif %}

    {% if list_view %}
         {{ post.fields.excerpt|linebreaks }}
         <footer>
              <p><a href="{{ post.get_absolute_url }}">{% trans "Read More" %}</a></p>
         </footer>
    {% endif %}


.. _post_type_rss_template:

tumblelog/rss/<post_type>.html
==============================

This template is used to display the body of posts of this type in the RSS feed. If this file does not exist, the :ref:`post type template <post_type_post_template>` is used.

Context
-------

- ``{{ post }}`` - A single ``Post`` object. See the :ref:`Post class documentation <post_class>` for more details on its fields and properties.

Example
-------

tumblelog does not come with any RSS templates. This examples shows what a template for the :ref:`article post type <article_post_type>` might look like, if you only wanted to show the excerpt. This template would be located at ``tumblelog/rss/article.html``.

::

    {{ post.fields.excerpt|linebreaks }}
    <p><a href="{{ post.get_absolute_url }}">{% trans "Read More" %}</a></p>
