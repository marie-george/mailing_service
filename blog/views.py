from django.views import generic
from django.urls import reverse, reverse_lazy


from blog.models import Blog
from blog.templates.blog.forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data

    def get_object(self, **kwargs):
        views = super().get_object()
        views.increase_view_count()
        return views


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('name', 'contents', 'preview')

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


