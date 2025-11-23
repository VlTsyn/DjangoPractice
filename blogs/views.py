from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'description', 'image']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'description']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
