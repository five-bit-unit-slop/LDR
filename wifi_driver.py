import network
import socket
import time
import json

PORT = 8080
BUFFER_SIZE = 1024
SERVER_IP = "192.168.137.1"
SENDER = None  # Global variable to store the sender address for responses

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        time.sleep(0.1)

    print("Connected:", wlan.ifconfig())
    return wlan

def send_data(data):
    global SERVER_IP, PORT, BUFFER_SIZE, SENDER
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.settimeout(3)

    try:
        payload = json.dumps(data).encode("utf-8")
        udp.sendto(payload, (SERVER_IP, PORT))
        response, SENDER = udp.recvfrom(BUFFER_SIZE)
        return response.decode("utf-8")
    
    except OSError as e:
        print("UDP error:", e)
        return None
    
    finally:
        udp.close()

