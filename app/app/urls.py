from django.contrib import admin
from django.urls import path

from shop.views import FitnessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FitnessView.FitnessView.as_view()),
]
