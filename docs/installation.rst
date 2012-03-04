Installation
============
Installing tumblelog is simple with `pip <http://www.pip-installer.org/en/latest/index.html>`_.

::

    $ pip install django-tumblelog

Quickstart
----------

Add tumblelog to ``INSTALLED APPS`` in your settings module:

::

    INSTALLED_APPS = [
        'django.contrib.contenttypes',
        ...
        'tumblelog',
    ]

Create the necessary database tables, using either ``syncdb`` or ``migrate`` (if using `South <http://south.aeracode.org/>`_).

::

    $ python manage.py syncdb
    $ python manage.py migrate tumblelog

Add a :ref:`TUMBLELOG_POST_TYPES <tumblelog_post_types_setting>` setting to your settings module, e.g.

::

    TUMBLELOG_POST_TYPES = [
        'tumblelog.contrib.text.Text',
        'tumblelog.contrib.photo.Image',
        'recipes.models.Recipe',
    ]

Finally, include the tumblelog URLconf to your ``urls`` module. The regex may be modified as you wish.

::

    url(r'^tumblelog/', include('tumblelog.urls', namespace='tumblelog')),

Requirements
------------

Django 1.4 is required (for `list filters <https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter>`_), and ``django.contrib.contenttypes`` must be installed.

Dependencies
------------

Tumblelog has two dependencies:

- `python-oembed <https://github.com/abarmat/python-oembed>`_ 0.2.1
- The latest version of the `Python Imaging Library <http://www.pythonware.com/products/pil/>`_

Source Code
-----------

tumblelog is developed on GitHub, where you can fork the repository, `browse the code <https://github.com/chuckharmston/django-tumblelog>`_, and `report issues <https://github.com/chuckharmston/django-tumblelog/issues>`_.

You can use pip to install the bleeding-edge code from the repository:

::

    $ pip install -e git+https://github.com/chuckharmston/django-tumblelog.git#egg=django-tumblelog

Alternatively, you can `download a tarball <https://github.com/chuckharmston/django-tumblelog/tarball/master>`_ or clone the repository:

::

    $ git clone git://github.com/chuckharmston/django-tumblelog

And install using ``setup.py``:

::

    $ python setup.py install
