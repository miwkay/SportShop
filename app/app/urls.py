from django.contrib import admin
from django.urls import path

from shop.views.BaseView import ShopMainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShopMainPage, name='ShopMainPage'),
]
