from django.contrib import admin
from django.urls import path

from shop.views.BaseView import fitness_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fitness_view, name='ShopMainPage'),
]
