from django.shortcuts import render

from shop.models.Fitness import Fitness


def ShopMainPage(request):
    fitness = Fitness.objects.all()
    return render(request, "shop/index.html", {'fitness': fitness})
