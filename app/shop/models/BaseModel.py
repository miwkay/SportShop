from django.db import models
import uuid
from django.utils import timezone
import Brand


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    set = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created', ]

    @property
    def price_display(self):
        return "$%s" % self.price
