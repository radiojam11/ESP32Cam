import esp32
from machine import Pin

r = esp32.RMT(0, pin=Pin(18), clock_div=8)
r   # RMT(channel=0, pin=18, source_freq=80000000, clock_div=8)
# The channel resolution is 100ns (1/(source_freq/clock_div)).
r.write_pulses((1, 20, 2, 40), start=0) # Send 0 for 100ns, 1 for 2000ns, 0 for 200ns, 1 for 4000ns

"""
The RMT is ESP32-specific and allows generation of accurate digital pulses with 12.5ns resolution. See esp32.RMT for details. Usage is:
"""