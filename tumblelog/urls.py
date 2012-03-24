from django.conf.urls.defaults import *

from tumblelog.feeds import PostFeed
from tumblelog.views import PostDetailView, PostListView

urlpatterns = patterns('tumblelog.views',
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^feed/$', PostFeed(), name="feed"),
    url(r'^(?P<slug>.+)/$', PostDetailView.as_view(), name="detail"),
)
