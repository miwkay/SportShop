from django.utils import timezone

from django.db import models
from shop.models.Product import Product


class Basket(models.Model):
    email = models.EmailField(('email address'), unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f"{self.product} {self.email} {self.phone} {self.date}"
