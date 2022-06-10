from django.shortcuts import render

from shop.models.WeightLifting import WeightLifting


def weight_lifting_view(request):
    weight_lifting = WeightLifting.objects.all()
    return render(request, "shop/WeightLifting.html", {'weight_lifting': weight_lifting})
