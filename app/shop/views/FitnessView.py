from django.views.generic import ListView

from Django.SportShop.app.shop.models import Fitness


class FitnessView(ListView):
    model = Fitness
    template_name = 'html/index.html'
