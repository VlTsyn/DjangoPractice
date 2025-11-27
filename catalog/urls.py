from django.urls import path
from .views import CatalogListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]