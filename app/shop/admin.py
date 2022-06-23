from django.contrib import admin

from shop.models.Category import Category
from shop.models.Product import Product
from shop.models.Brand import Brand
from shop.models.Basket import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'phone', 'date']
admin.site.register(Basket, BasketAdmin)

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)




