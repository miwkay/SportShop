from django.contrib import admin
from django.urls import path, include

from shop.views.BrandView import brand_view
from shop.views.MainView import main_view
from shop.views.ProductView import product_view
from shop.views.BasketView import product, saveorder


urlpatterns = [
    path('', main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('brand/', brand_view, name='brand_view'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('product/', product_view),
    path('product/<uuid:id>/', product),
    path('saveorder', saveorder),

]
