from django.contrib import admin
from django.urls import path, include

from shop.views.BrandView import brand_view
from shop.views.MainView import main_view
from shop.views.ChildrensView import childrens_view
from shop.views.FitnessView import fitness_view
from shop.views.SportNutritionView import sport_nutrition_view
from shop.views.SportsSimulatorView import sports_simulator_view
from shop.views.TourismView import tourism_view
from shop.views.WeightLiftingView import weight_lifting_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('brand/', brand_view, name='brand_view'),
    # path('product/?<category:str>/', product_view, name="product_view")
    path('childrens/', childrens_view, name='childrens_view'),
    path('fitness/', fitness_view, name='fitness_view'),
    path('sportnutrition/', sport_nutrition_view, name='sport_nutrition_view'),
    path('sportssimulator/', sports_simulator_view, name='sports_simulator_view'),
    path('tourism/', tourism_view, name='tourism_view'),
    path('weightlifting/', weight_lifting_view, name='weight_lifting_view'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

]
