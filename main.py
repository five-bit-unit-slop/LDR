from machine import Pin, ADC
import utime
import json
from wifi_driver import connect_wifi, send_data

ldr = ADC(Pin(26))
draaiknop = ADC(Pin(27))

def timestamp_now():
    t = utime.localtime()
    return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(
        t[0], t[1], t[2], t[3], t[4], t[5]
    )

device_token = "YOUR_REAL_DEVICE_TOKEN"

while True:
    data = {
        "version": "1.0",
        "request_id": str(utime.ticks_ms()),
        "timestamp": timestamp_now(),
        "device": {
            "id": "pico-001"
        },
        "action": "sensor.measurement",
        "payloads": 
        {   1: {
                "sensor": "light",
                "value": ldr.read_u16(),
                "unit": "raw",
            },
            2: {
                "sensor": "draaiknop",
                "value": draaiknop.read_u16(),
                "unit": "raw",
            }

        },
        "auth": {
            "token": device_token
        }
    }

    response = send_data(data)
    if response is not None:
        print("Server response:", response)

    value_LDR = ldr.read_u16
    value_draaiknop = draaiknop.read_u16

    

