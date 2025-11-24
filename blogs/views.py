from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blogs:blog_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Blog.objects.filter(pk=obj.pk).update(views_count= obj.views_count + 1)
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'publication']
    template_name = 'blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blogs:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blog_list')
