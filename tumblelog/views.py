from django.template.defaultfilters import slugify
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tumblelog.models import Post


class PostListView(ListView):
    allow_empty = False
    context_object_name = 'posts'
    paginate_by = 20
    queryset = Post.objects.public()


class PostDetailView(DetailView):
    context_object_name = 'post'
    queryset = Post.objects.public()

    def get_post_template(self, model):
        return 'tumblelog/%s_detail.html' % slugify(model)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        obj = context['object']
        context.update({
            'template': self.get_post_template(obj.fields.__class__.__name__)
        })
        return context
