from machine import Pin, ADC
from utime import sleep_ms

ldr = ADC(Pin(26))

while True:
    val = ldr.read_u16()
    print(val)
    sleep_ms(1000)      