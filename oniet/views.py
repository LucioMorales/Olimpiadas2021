from django.shortcuts import render
from .models import *

# Create your views here.

def homeview(request):

    store = Store.objects.all()

    context = {
        "store": store
    }

    return render(request, "customer.html", context)

def managerview(request):

    store = Store.objects.all()

    context = {
        "store": store
    }

    return render(request,"manager.html",context)