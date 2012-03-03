from django.conf.urls.defaults import *

from tumblelog.views import PostDetailView, PostListView

urlpatterns = patterns('tumblelog.views',
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^(?P<slug>.+)/$', PostDetailView.as_view(), name="detail"),
)
