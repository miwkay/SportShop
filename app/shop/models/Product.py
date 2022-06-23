from django.db import models
import uuid
from django.utils import timezone
from shop.models.Category import Category
from shop.models.Brand import Brand


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    set = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now, db_index=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created', ]
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    @property
    def price_display(self):
        return "$%s" % self.price

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
