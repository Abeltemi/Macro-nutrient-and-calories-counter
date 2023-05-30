from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class Consume(models.Model):
    
    def __str__(self):
        return self.consumed_user.username
    
    food_consumed_by_user = models.ForeignKey(Food, on_delete=models.CASCADE, default=None, null=True)
    consumed_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    