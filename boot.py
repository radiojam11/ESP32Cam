# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import webrepl
webrepl.start()
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('PosteMobile_0A3220_2.4G', '32170320')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()