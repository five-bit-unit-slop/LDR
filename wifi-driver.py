import network
import time

def connect_wifi(ssid, password):
    print(f"Connecting to {ssid}...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        time.sleep(1)

    print("Connected!")
    return wlan
