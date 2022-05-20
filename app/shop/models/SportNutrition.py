from django.db import models
from kombu.utils import uuid


class SportNutrition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    set  = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
