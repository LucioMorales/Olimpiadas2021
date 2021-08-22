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

#dynamic html para descuentos


def discountsview(request, localN):
    
    localname = Store.objects.get(name=localN)

    store = Store.objects.all()

    context = {
    "store": store,
    "localname": localname
    }

    return render(request, 'discounts.html', context)