from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def main_page(request):
    if request.method == "POST":
        brand = request.POST.get('brand','')
        name = request.POST.get('car_name','')
        price = request.POST.get('price','')
        date_release = request.POST.get('date_release','')
        fuel= request.POST.get('cars_fuel','')
        system = request.POST.get('cars_system','')

        cars = Car(car_company = brand.capitalize(),
                   car_company_name = name.capitalize(),
                   price=price, 
                   release_date = date_release, 
                   fuel=fuel,
                   system=system)
        cars.save()

    return render(request,'main.html')

def page_1(request):
    # return HttpResponse("Hello Django")
    # Cars = Car.objects.all()
    Cars = Car.objects.values('car_company')
    cars = {items['car_company'] for items in Cars}
    parameters = {
        'cars':cars
    }
    return render(request, "car_brand.html",parameters)


def detail(request,company):
    cars = Car.objects.filter(car_company = company)
    car = {item['car_company_name'] for item in cars.values()}
    car_brand = company
    parameters = {
        'cars':car,
        'car_brand':car_brand
    }
    return render(request, "car_detail.html",parameters)


def detail_2(request,company,name):
    car = Car.objects.filter(car_company_name = name, car_company = company)
    cars = company
    parameters = {
        'car':car,
        'car_name':cars
    }
    return render(request, "car_detail_2.html",parameters)


def test(request):
    data = Car.objects.values()
    head = []
    for i in data:
        for key in i:
            if key not in head:
                head.append(key)

    car = Car.objects.all().order_by('car_company','price')
    parameters = {
        'car':car,
        'head':head
    }
    return render(request, "test.html",parameters)
