from gpiozero import LED
from time import sleep

led = LED(10) # assign GPIO pin 10 to led variable

# ---------turn led on and off with 0.1sec interval
while True:            
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
# ---------turn led on and off with 0.1sec interval
