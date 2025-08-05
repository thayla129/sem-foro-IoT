from machine import Pin
from utime import sleep

ledVerde = Pin(15, Pin.OUT)
ledAmarelo = Pin(16, Pin.OUT)
ledVermelho = Pin(17, Pin.OUT)

while True:
    ledVerde.on()
    ledAmarelo.off()
    ledVermelho.off()
    print('Verde - Ligado por 20 segundos')
    sleep(20)
    ledVerde.off()
    sleep(0.5)

    ledAmarelo.on()
    print('Amarelo - Ligado por 10 segundos')
    sleep(10)
    ledAmarelo.off()
    sleep(0.5)

    ledVermelho.on()
    print('Vermelho - Ligado por 7 segundos')
    sleep(7)
    ledVermelho.off()
    sleep(0.5)
