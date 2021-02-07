# per poter gestire la connessione durante l'esecuzione dei programmi e' forse meglio portare 
# la funzione di connessione WIFI dentro il main. se utilizzato controllare che sia eliminata da boot.py.
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