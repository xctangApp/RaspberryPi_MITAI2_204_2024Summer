# this only works on Pi4 system

import RPi.GPIO as GPIO  #import GPIO library
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  #use hte BOARD mode reference physical numbering
GPIO.setup(19,GPIO.OUT)

try:
    while True:
        GPIO.output(19, 1)  # turn on the LED
        time.sleep(1)
        GPIO.output(19, 0)  # turn off the LED
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
