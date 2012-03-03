`django-tumblelog`: A simple and extensible tumblelog engine for Django. Created by Chuck Harmston, released under the [MIT license](https://github.com/chuckharmston/django-tumblelog/blob/master/LICENSE).

View full documentation at [http://rtfd.org/django-tumblelog](rtfd.org/django-tumblelog)

# Overview

Jason Kottke [defined](http://www.kottke.org/05/10/tumblelogs) tumblelogs as:

>a quick and dirty stream of consciousness, a bit like a remaindered links style linklog but with more than just links [...] with minimal commentary, little cross-blog chatter, the barest whiff of a finished published work, almost pure editing...really just a way to quickly publish the "stuff" that you run across every day on the web. [They have] different ways of displaying various types of content...remaindered links, regular posts, book reviews, and movie reviews are all displayed differently.

Perhaps the best implementation of this model is [Tumblr](http://tumblr.com), a simple hosted tumblelog service that allows you to post text snippets, photos, quotes, links, chat logs, audio files, or video files. While an excellent service, it is a bit limiting; post formats are restricted to those seven things. If you would like a standard format to your recipes or code snippets, you're out of luck. 

`django-tumblelog` is an attempt to provide more flexibility to the tumblelog format.

## Post Types

Post types are subclasses of `tumblelog.models.BasePostType`, which itself is a subclass of Django's `db.models.Model`. This allows each post type to contain fields specific to its purpose, giving you extreme flexibility over the structure and format of your data. Let's look at an example post type for recipes:

    from django.db import models
    from django.utils.translation import ugettext as _

    from tumblelog.models import BasePostType

    class Recipe(BasePostType):
        """
        Post type for a recipe.
        """
        intro = models.TextField(_('Introduction'))
        prep_time = models.CharField(_('Preparation Time'), max_length=128)
        cook_time = models.CharField(_('Cooking Time'), max_length=128)
        recipe_yield = models.CharField(_('Yield'), max_length=128)
        ingredients = models.TextField(_('Ingredients'))
        directions = models.TextField(_('Directions'))

        class TumblelogMeta:
            prepopulated_fields = {
                'slug': ('title',)
            }

You then register this post type with tumblelog using a property in your settings module:"

    TUMBLELOG_POST_TYPES = [
        'tumblelog.contrib.text.Text',
        'recipes.models.Recipe',
    ]

That's all there is to it! A few things to note:
1. The `Recipe` class inherits from `BasePostType`.
2. Fields for `title`, `slug`, `date_published`, and `status` are already defined by `BasePostType`
3. You do not need to create a `ModelAdmin` for post type classes. Instead, you define admin properties on inner class `TumblelogMeta` (as is done for `prepopulated_fields`), which is used to generate a `ModelAdmin`.
4. Subclasses of `BasePostType` can be defined in any models.py file. This allows you to manage the database table however you see fit (though it's recommended that you use South).

## Posts

It's not especially useful to use the ORM to query a single post type at a time, as the point is to 

 Enter the `Post` object, which is created and synchronized with each save of an instance of a subclass of  `BasePostType`. This allows you to query instances of all post types, sorting and filtering on common fields.
 
    >>> from tumblelog.models import Post
    >>> Post.objects.public()
    [<Post: Deboning Pony Legs (Text)>, <Post: Crostini with Pony Tartare (Recipe)>, <Post: Pony Au Poivre (Recipe)>, <Post: Pony Stew with Dried Plums (Recipe)>]
 
Note that the query returned instances of both `Text` and `Recipe` post types. 

## oEmbed Post Types

Frequently, tumblelog authors embed content from third party sites. `django-tumblelog` providers helpers for interfacing with content on websites implementing [oEmbed](http://oembed.com), a standard which allows metadata retrieval and an embedded representation of a URL on third party sites.

By taking the URL of a YouTube video, tumblelog can pull the latest YouTube embed code, a preview thumbnail, and other associated metadata.

## Contrib post types

You aren't left to implement all the necessary post types; `django-tumblelog` includes batteries for many basic needs. The `tumblelog.contrib` model contains a number basic post types, including: 

* Text snippet (`tumblelog.contrib.text.Text`)
* Long-form article (`tumblelog.contrib.text.Article`)
* Link (`tumblelog.contrib.link.Link`)
* File (`tumblelog.contrib.file.File`)
* Image (`tumblelog.contrib.photo.Image`)

Additionally, we've implemented some of the most common oEmbed providers:

* YouTube (`tumblelog.contrib.video.YouTube`)
* Vimeo (`tumblelog.contrib.video.Vimeo`)
* Twitter (`tumblelog.contrib.twitter.Tweet`)
* Instagram (`tumblelog.contrib.photo.Instagram`)
* Flickr (`tumblelog.contrib.photo.Flickr`)
* GitHub Gist (`tumblelog.contrib.code.Gist`)
* SoundCloud (`tumblelog.contrib.audio.SoundCloud`)
* Rdio (`tumblelog.contrib.audio.Rdio`)