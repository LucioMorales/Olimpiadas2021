from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.homeview, name = "customer"),
    path('adminsite/', views.managerview, name = "adminsite"),
    path('discounts/<str:localN>/',views.discountsview, name='localname'),
]