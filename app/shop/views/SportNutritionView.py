from django.shortcuts import render

from shop.models.SportNutrition import SportNutrition


def sport_nutrition_view(request):
    sport_nutrition = SportNutrition.objects.all()
    return render(request, "shop/SportNutrition.html", {'sport_nutrition': sport_nutrition})
