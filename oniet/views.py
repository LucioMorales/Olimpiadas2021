from django.shortcuts import render
from .models import *
import pyfirmata
import time 

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


def addPeople(pk):

    board = pyfirmata.Arduino('/dev/ttyACM0')

    button = board.digital[8]
    previous_button_state = 0
    ##BUTTON_PIN = board.get_pin('d:8:i')

    it = pyfirmata.util.Iterator(board)
    it.start()

    button.mode = pyfirmata.INPUT

    store = Store.objects.get(id=1)
    
    ca = Store.objects.get()

    while True:

        time.sleep(0.01)
        
        button_state = button.read()
        
        if button_state != previous_button_state:
            if button_state == 0:
                store.currentAmount = +1;
                store.currentAmount.save()
                print(store)

        previous_button_state = button_state
