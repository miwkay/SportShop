from shop.models.BaseModel import BaseModel


class SportNutrition(BaseModel):
    pass

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price}"
