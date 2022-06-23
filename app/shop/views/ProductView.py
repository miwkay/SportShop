from django.shortcuts import render

from shop.models.Product import Product


def product_view(request):
    product = Product.objects.all()
    return render(request, "shop/Product.html", {'product': product})
