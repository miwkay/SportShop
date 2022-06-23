from django.shortcuts import render

from shop.models.Basket import Basket
from shop.models.Childrens import Childrens


def product(request, id):
    product = Childrens.objects.get(pk=id)
    return render(request, 'shop/Product.html', {"product": product})


def saveorder(request):
    product = Childrens.objects.get(pk=request.POST['product_id'])
    b = Basket()
    b.name = request.POST['username']
    b.phone = request.POST['phone']
    b.product = product
    b.save()
    return render(request, 'shop/Product.html', {"product": product})
