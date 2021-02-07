import machine

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# put the device to sleep for 10 seconds
machine.deepsleep(10000)

"""
Calling deepsleep() without an argument will put the device to sleep indefinitely

A software reset does not change the reset cause

There may be some leakage current flowing through enabled internal pullups. To further reduce power consumption it is possible to disable the internal pullups:

p1 = Pin(4, Pin.IN, Pin.PULL_HOLD)
After leaving deepsleep it may be necessary to un-hold the pin explicitly (e.g. if it is an output pin) via:

p1 = Pin(4, Pin.OUT, None)
"""