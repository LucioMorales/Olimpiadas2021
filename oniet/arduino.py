
import pyfirmata
import time 
board = pyfirmata.Arduino('/dev/ttyACM0')



button = board.digital[8]
previous_button_state = 0
##BUTTON_PIN = board.get_pin('d:8:i')

it = pyfirmata.util.Iterator(board)
it.start()

button.mode = pyfirmata.INPUT

while True:
        # We run the loop at 100Hz
        time.sleep(0.01)
        
        # Get button current state
        button_state = button.read()
        
        # Check if button has been released
        if button_state != previous_button_state:
            if button_state == 0:
                print("Button released")

        previous_button_state = button_state

