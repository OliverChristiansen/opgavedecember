from machine import TouchPad, Pin
from time import sleep

touch = TouchPad(Pin(0, Pin.IN))

RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)

YELLOW_PIN = 12
led2 = Pin(YELLOW_PIN, Pin.OUT)

GREEN_PIN = 13
led3= Pin(GREEN_PIN, Pin.OUT)

while True:
    print(touch.read())
    sleep(0.5)
    if touch.read() < 150:
        print("Touch activated")
        led1.on()
        led2.off()
        led3.on()
        while touch.read() < 150:
            led1.value(not led1.value())
            led2.value(not led2.value())
            led3.value(not led3.value())
            sleep(0.5)
    
    elif touch.read() > 150:
        led1.off()
        led2.on()
        led3.off()
        