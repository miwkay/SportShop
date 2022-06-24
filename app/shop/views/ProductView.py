from django.shortcuts import render

from shop.models.Product import Product
from shop.models.Category import Category


def product_view(request):
    product = Product.objects.all()
    return render(request, "shop/AllProduct.html", {'product': product})


def category_view(request):
    category = Category.objects.all()
    return render(request, "shop/Category.html", {'category': category})
