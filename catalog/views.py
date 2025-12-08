from itertools import product

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
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



class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
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


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
