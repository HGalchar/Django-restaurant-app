from django.db import models

# Create your models here.
class addRestaurants(models.Model):

    R_name=models.CharField(max_length=100)
    R_ownername=models.CharField(max_length=100)
    R_mobileno=models.CharField(max_length=20)
    R_adress=models.CharField(max_length=100)
    R_type=models.CharField(max_length=20)

def __str__(self):
     return self.R_name

class addMenu(models.Model):

    Restaurant = models.ForeignKey(addRestaurants ,null=False, on_delete=models.CASCADE)
    Dish_name=models.CharField(max_length=100)
    Dish_type=models.CharField(max_length=50)
    Dish_price=models.CharField(max_length=20)