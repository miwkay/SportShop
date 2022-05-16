from django.db import models


class DumbbellsMono(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} - {self.weight}"
