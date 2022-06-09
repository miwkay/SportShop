from django.shortcuts import render

from shop.models.Fitness import Fitness


def fitness_view(request):
    fitness = Fitness.objects.get()
    return render(request, "shop/index.html", {'fitness': fitness})
