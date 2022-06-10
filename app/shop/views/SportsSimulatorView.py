from django.shortcuts import render

from shop.models.SportsSimulator import SportsSimulator


def sports_simulator_view(request):
    sports_simulator = SportsSimulator.objects.all()
    return render(request, "shop/SportsSimulator.html", {'sports_simulator': sports_simulator})
