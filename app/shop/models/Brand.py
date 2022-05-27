from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
