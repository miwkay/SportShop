import BaseModel
from django.db import models


class Childrens(BaseModel):
    ...

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
