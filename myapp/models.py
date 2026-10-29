from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    """Catalog of available foods with their macro values."""
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    """A logged food entry — references the Food catalog."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    servings = models.FloatField(default=1.0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.food.name} x{self.servings}"

    @property
    def calories(self):
        return round(self.food.calories * self.servings)

    @property
    def protein(self):
        return round(self.food.protein * self.servings, 1)

    @property
    def carbs(self):
        return round(self.food.carbs * self.servings, 1)

    @property
    def fat(self):
        return round(self.food.fat * self.servings, 1)