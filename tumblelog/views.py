from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tumblelog.models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 2
    queryset = Post.objects.public()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'list_view': True,
            'detail_view': False,
        })
        return context


class PostDetailView(DetailView):
    context_object_name = 'post'
    queryset = Post.objects.public()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'list_view': False,
            'detail_view': True,
        })
        return context
