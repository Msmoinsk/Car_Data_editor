from django.contrib import admin
from .models import Car
# Register your models here.

class Car_excel(admin.ModelAdmin):
    list_display = ('car_company', 'car_company_name','price','release_date')

admin.site.register(Car, Car_excel)