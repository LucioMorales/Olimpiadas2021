from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.homeview, name = "customer"),
    path('manager/', views.managerview, name = "manager"),
]