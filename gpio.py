from machine import Pin
import time

#gestione del LED rpincipale Bianco della scheda sul GPIO4
LEDb = Pin(4, Pin.OUT) 
while True:
    LEDb.value(1)
    time.sleep_ms(500)
    LEDb.value(0)
    time.sleep_ms(500)

#gestione del LED di servizio Rosso della scheda sul GPIO33
LEDr = Pin(33, Pin.OUT) 
while True:
    LEDr.value(1)
    time.sleep_ms(500)
    LEDr.value(0)
    time.sleep_ms(500)

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation