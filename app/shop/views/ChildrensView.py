from django.shortcuts import render

from shop.models.Childrens import Childrens


def childrens_view(request):
    childrens = Childrens.objects.all()
    return render(request, "shop/Childrens.html", {'childrens': childrens})
