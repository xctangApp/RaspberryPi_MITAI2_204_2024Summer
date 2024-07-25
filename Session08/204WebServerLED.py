#----------------------------------------------------------------
#
#             LED Control from android app
#
#In this program, LED on Rpi will be connected through 
#GPIO2, below code work with android app,will turn the LED on/off 
#
#Program:204WebServerLED.py
#Date:07/24/2024
#Author: X.Tang
#Version: 1.0  Intial
#  1.1  Add ...
#-----------------------------------------------------------------

from flask import Flask, render_template   # import flask web server library
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # set BCM logical pin numbering

LED  = 2                     # define LED on GPIO2
GPIO.setup(LED, GPIO.OUT)    # define output pin
GPIO.output(LED, 0)          # turn off LED to start

#
#start the main program loop, read command from android app
#through local web server, decode the msg and control LED
#

@app.route("/<device>/<action>")

def action(device, action):
    actuator = LED
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)  # turn on LED
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)   # turn off LED
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)
