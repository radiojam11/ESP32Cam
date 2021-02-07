from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(16, Pin.OUT)   # set GPIO16 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
while True:
    for i in range(8):
        np[i] = (25, 5, 5)      # set the first pixel to orange
        np.write()              # write data to all pixels
        time.sleep_ms(500)
    for i in range(8, 0, -1):
        np[i-1] = (0, 0, 0)      # set the first pixel to orange
        np.write()              # write data to all pixels
        time.sleep_ms(500)
