from django.shortcuts import render

from shop.models.Product import Product


def product_view(request, **kwargs):
    products = Product.objects.all()

    if 'category' in kwargs:
        category = kwargs['category']
        products = products.filter(category=category)
    else:
        category = None

    return render(request, "shop/Childrens.html", {'category': category, 'products': products})
