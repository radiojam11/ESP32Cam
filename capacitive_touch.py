from machine import TouchPad, Pin

t = TouchPad(Pin(14))
t.read()              # Returns a smaller number when touched

"""
Note that TouchPads can be used to wake an ESP32 from sleep:

import machine
from machine import TouchPad, Pin
import esp32

t = TouchPad(Pin(14))
t.config(500)               # configure the threshold at which the pin is considered touched
esp32.wake_on_touch(True)
machine.lightsleep()        # put the MCU to sleep until a touchpad is touched

"""