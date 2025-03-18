# main.py -- put your code here!
from machine import Pin
from time import sleep
from machine import mem32

peatonal1verde=Pin(23,Pin.OUT)
peatonal2verde=Pin(22,Pin.OUT)
peatonal3verde=Pin(21,Pin.OUT)
vehicular4amarillo=Pin(19,Pin.OUT)
vehicular5verde=Pin(18,Pin.OUT)
vehicular6verde=Pin(5,Pin.OUT)
peatonal1rojo=Pin(13,Pin.OUT)
peatonal2rojo=Pin(12,Pin.OUT)
peatonal3rojo=Pin(14,Pin.OUT)
vehicular4rojo=Pin(27,Pin.OUT)
vehicular5rojo=Pin(26,Pin.OUT)
vehicular6rojo=Pin(25,Pin.OUT)

global pare
pare=0

global temperatura
temperatura=0

def interrupcion_pare(Pin):
    global pare
    print("Entre a la funcion interrupcion")
    pare=1

def interrupcion(Pin):
    global temperatura
    print("Entre a la funcion interrupcion")
    temperatura=1

pare=Pin(33,Pin.IN)
pare.irq(trigger=Pin.IRQ_RISING, handler=interrupcion_pare)

GPIO_SET=const(0x3FF44004)

while True:
    mem32[GPIO_SET]=0b00010010011000110000000000000
    sleep(6.8)
    mem32[GPIO_SET]=0b00010000010000110000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b00010010011000110000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b00010000010000110000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b00010010011000110000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b00010000010000110000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b00010010011000110000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b00010000010000110000000000000
    sleep(0.1)
    mem32[GPIO_SET]=0b00010010011000110000000000000
    sleep(0.1)
    mem32[GPIO_SET]=0b00100100010000101000000100000
    sleep(6.8)
    mem32[GPIO_SET]=0b00100000000000101000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b00100100010000101000000100000
    sleep(0.5)
    mem32[GPIO_SET]=0b00100000000000101000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b00100100010000101000000100000
    sleep(0.3)
    mem32[GPIO_SET]=0b00100000000000101000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b00100100010000101000000100000
    sleep(0.2)
    mem32[GPIO_SET]=0b00100000000000101000000000000
    sleep(0.1)
    mem32[GPIO_SET]=0b00100100010000101000000100000
    sleep(0.1)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(4.8)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.1)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.1)

    if pare==1:
        mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(4.8)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.3)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.2)
    mem32[GPIO_SET]=0b01110000000000000000000000000
    sleep(0.1)
    mem32[GPIO_SET]=0b01110111000000000000000000000
    sleep(0.1)
    pare=0
