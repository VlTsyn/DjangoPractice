from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/<int:pk>/', views.product_detail, name='product_detail')
]