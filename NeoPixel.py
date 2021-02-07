from machine import Pin
from neopixel import NeoPixel

pin = Pin(16, Pin.OUT)   # set GPIO16 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (25, 5, 5)      # set the first pixel to orange
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour


"""
For low-level driving of a NeoPixel:

import esp
esp.neopixel_write(pin, grb_buf, is800khz)
###############
Warning

By default NeoPixel is configured to control the more popular 800kHz units. It is possible to use alternative timing to control other (typically 400kHz) 
devices by passing timing=0 when constructing the NeoPixel object.
"""