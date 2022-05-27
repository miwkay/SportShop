from django.db import models
import BaseModel


class SportNutrition(BaseModel):
    ...


    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
