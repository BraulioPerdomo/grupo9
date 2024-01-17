#1.- obtener la temperatura
#2.- grabarla en la base de datos

import leerSensorTemperatura
import grabarEnBaseDeDatos
from time import sleep

while True:
    leerSensorTemperatura.leerTemperatura()
    print(f"Temperatura: {leerSensorTemperatura.temperatura}")
    print(f"Humedad: {leerSensorTemperatura.humedad}")
    grabarEnBaseDeDatos.GrabarTemperaturaYHumedad(leerSensorTemperatura.temperatura, leerSensorTemperatura.humedad)
    sleep(5)