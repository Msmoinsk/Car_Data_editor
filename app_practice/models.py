from django.db import models

# Create your models here.
class Car(models.Model):
    car_company = models.CharField(max_length = 100)
    car_company_name = models.CharField(max_length = 100)
    release_date = models.DateField(null = True)
    price = models.IntegerField(null=True)
    fuel = models.CharField(max_length = 10,null=True)
    system = models.CharField(max_length = 20, null=True)
