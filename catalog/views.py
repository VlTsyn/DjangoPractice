from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import products_by_category


class CategoriesMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductsByCategoryView(CategoriesMixin, ListView):
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products_by_category'

    def get_queryset(self):
        """Получаем товары по категории"""
        category = self.kwargs.get('category')
        return products_by_category(category)

    def get_context_data(self, **kwargs):
        """Добавляем категорию в контекст"""
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')

        context['category'] = get_object_or_404(Category, id=category)

        return context


class ProductCreateView(LoginRequiredMixin, CategoriesMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CategoriesMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    permission_required = 'catalog:can_unpublish_product'

    def has_permission(self):
        product = self.get_object()
        user = self.request.user

        if product.owner == user:
            return True

        return super().has_permission()


class CatalogListView(CategoriesMixin, ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


# @method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(CategoriesMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, CategoriesMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')
    permission_required = 'catalog.delete_product'

    def has_permission(self):
        product = self.get_object()
        user = self.request.user

        if product.owner == user:
            return True

        return super().has_permission()


class ContactsView(CategoriesMixin, TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
