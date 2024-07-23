from gpiozero import Button

btn = Button(2)

def hello():
    print("hello")

btn.when_pressed = hello
