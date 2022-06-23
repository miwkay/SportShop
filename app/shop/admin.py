from django.contrib import admin

from shop.models.Fitness import Fitness
from shop.models.SportNutrition import SportNutrition
from shop.models.WeightLifting import WeightLifting
from shop.models.Childrens import Childrens
from shop.models.SportsSimulator import SportsSimulator
from shop.models.Tourism import Tourism
from shop.models.Brand import Brand
from shop.models.Basket import Basket


admin.site.register(Brand)
admin.site.register(Fitness)
admin.site.register(SportNutrition)
admin.site.register(WeightLifting)
admin.site.register(Childrens)
admin.site.register(SportsSimulator)
admin.site.register(Tourism)


class BasketAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
admin.site.register(Basket, BasketAdmin)
