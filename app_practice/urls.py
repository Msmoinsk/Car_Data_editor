# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main"),
    path('car_brand/', views.page_1, name="brand"),
    path('car_brand/<str:company>/', views.detail, name="name"),
    path('car_brand/<str:company>/<str:name>/', views.detail_2, name="details"),
    path('test_case/', views.test, name="test_case"),
]