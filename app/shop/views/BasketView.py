from django.shortcuts import render

from shop.models.Basket import Basket
from shop.models.Product import Product

# from users.models import CustomUser

def product(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'shop/Product.html', {"product": product})


def saveorder(request):
    # user = CustomUser.objects.get(email='')
    # user.delete()
    product = Product.objects.get(pk=request.POST['product_id'])
    b = Basket()
    b.name = request.POST['username']
    b.phone = request.POST['phone']
    b.product = product
    b.save()
    return render(request, 'shop/Saveorder.html', {"product": product})
