
from .models import *
import pyfirmata
import time 

def addPeople(pk):

    board = pyfirmata.Arduino('/dev/ttyACM0')

    button = board.digital[8]
    previous_button_state = 0
    ##BUTTON_PIN = board.get_pin('d:8:i')

    it = pyfirmata.util.Iterator(board)
    it.start()

    button.mode = pyfirmata.INPUT

    store = Store.objects.get(pk=pk)
    ca = store.objects.get(pk=pk).currentAmount()

    while True:
        # We run the loop at 100Hz
        time.sleep(0.01)
        
        # Get button current state
        button_state = button.read()
        
        # Check if button has been released
        if button_state != previous_button_state:
            if button_state == 0:
                ca = +1;
                ca.save()
                print(ca)

        previous_button_state = button_state

