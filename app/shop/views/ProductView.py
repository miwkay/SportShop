from django.shortcuts import render

from shop.models.Product import Product
from shop.models.Brand import Brand


def product_view(request):
    product = Product.objects.all()
    return render(request, "shop/Product.html", {'product': product})


def all_product_view(request):
    product = Product.objects.all()
    return render(request, "shop/AllProduct.html", {'product': product})
