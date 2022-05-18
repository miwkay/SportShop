from django.views.generic import ListView

from Django.sporting_goods_store.sportinggoodsstore.dumbbells.models.fitness import Fitness


class FitnessView(ListView):
    model = Fitness
    queryset = Fitness.objects.all()
