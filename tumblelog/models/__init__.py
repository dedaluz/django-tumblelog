import sys

from tumblelog.models.base import Post
from tumblelog.models.contrib.audio import Rdio, SoundCloud
from tumblelog.models.contrib.code import Code, CodeSnippet, Gist
from tumblelog.models.contrib.file import File
from tumblelog.models.contrib.link import Link
from tumblelog.models.contrib.photo import Image, Flickr, Instagram
from tumblelog.models.contrib.text import Article, TextSnippet
from tumblelog.models.contrib.twitter import Tweet
from tumblelog.models.contrib.video import YouTube, Vimeo
from tumblelog.settings import POST_TYPES
from tumblelog.util import import_model

__all__ = [
    'Post',
    'Rdio',
    'SoundCloud',
    'Gist',
    'File',
    'Link',
    'Image',
    'Flickr',
    'Instagram',
    'Article',
    'TextSnippet',
    'Tweet',
    'YouTube',
    'Vimeo',
    'Code',
    'CodeSnippet',
]

for post_type in POST_TYPES:
    if not post_type.startswith('tumblelog.'):
        model = import_model(post_type)
        model_name = model.__name__
        setattr(sys.modules[__name__], model_name, model)
        __all__.append(model_name)
