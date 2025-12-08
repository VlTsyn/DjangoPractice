from .models import Product

def products_by_category(category):

    products = Product.objects.filter(category=category)

    return products