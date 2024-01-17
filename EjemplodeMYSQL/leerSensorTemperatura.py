temperatura = 0
humedad = 0

def leerTemperatura():
    global temperatura, humedad
    import random
    temperatura = random.uniform(0.0, 30.0)
    humedad = int(random.randrange(0,100, 1))