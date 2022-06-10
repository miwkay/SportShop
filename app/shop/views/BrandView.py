from django.shortcuts import render

from shop.models.Brand import Brand


def brand_view(request):
    brand = Brand.objects.all()
    return render(request, "shop/Brand.html", {'brand': brand})
