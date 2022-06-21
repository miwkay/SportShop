from django.utils import timezone

from django.db import models
from shop.models.Childrens import Childrens


class Basket(models.Model):
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    product = models.ForeignKey(Childrens, on_delete=models.CASCADE, default='', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email} {self.date}"
