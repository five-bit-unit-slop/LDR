from machine import Pin, ADC # pyright: ignore[reportMissingImports]
import utime # pyright: ignore[reportMissingImports]
import json
from wifi-driver import connect_wifi, send_data

ldr = ADC(Pin(26))

data = {
    "version": "1.0",
    "request_id": "uuid",
    "timestamp": "2026-11-04T20:00:00Z",
    "device": {
        "id": "pico-001"
    },
    "action": "sensor.measurement",
    "payload": {
        "sensor": "light",
        "value": 0,
        "unit": "raw"
    },
    "auth": {
        "token": "DEVICE_TOKEN"
    }
}

while True:
    val = ldr.read_u16()
    data["payload"]["value"] = val
    print(data)
    print(json.dumps(data, indent=4))
    utime.sleep(1)
