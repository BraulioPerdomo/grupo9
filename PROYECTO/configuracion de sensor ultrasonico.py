from gpiozero import LED, DistanceSensor
from time import sleep

LedMedioVacio = LED(14)
LedMedio = LED(15)
LedLleno = LED(18)
sensor = DistanceSensor(echo=24, trigger=23)

while True:
    distancia = sensor.distance * 100
    print ("distancia: ", distancia)
    if (distancia < 2.5):
        LedLleno.on()
        LedMedio.off() 
        LedMedioVacio.off()
    elif (distancia < 7.5):
        LedLleno.off()
        LedMedio.on() 
        LedMedioVacio.off()
    elif (distancia < 12.5):
        LedLleno.off()
        LedMedio.off() 
        LedMedioVacio.on()
    else:
        LedLleno.blink()
        LedMedio.blink() 
        LedMedioVacio.blink()
        sleep(2)
    
    
        
        
    