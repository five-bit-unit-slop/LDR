import network
import socket
import time
import json

PORT = 8080
BUFFER_SIZE = 1024
SERVER_IP = "192.168.1.100"

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        time.sleep(1)

    print("Connected:", wlan.ifconfig())
    return wlan

_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_udp.settimeout(3)

def send_data(data):
    payload = json.dumps(data).encode("utf-8")
    _udp.sendto(payload, (SERVER_IP, PORT))

    try:
        response, address = _udp.recvfrom(BUFFER_SIZE)
        return response.decode("utf-8")
    except OSError:
        return None
