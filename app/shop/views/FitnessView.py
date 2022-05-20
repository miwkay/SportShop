from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Fitness


class FitnessView(ListView):
    model = Fitness
    template_name = 'shop/index.html'

