velocidadDeParpadeo = 1

def leerConfiguracion():
    global velocidadDeParpadeo

    f = open("configuracion.ini", "r")
    lineas = f.readlines()

    #print(lineas)
    for linea in lineas:
        datos = linea.split('=')
        if (datos[0] == "velocidad"):
            velocidadDeParpadeo = int(datos[1])
        #print(datos)
    f.close()

def grabarConfiguracion():
    f = open("configuracion.ini", "w")
    f.write("velocidad="+str(velocidadDeParpadeo)+"\r")
    f.close()


leerConfiguracion()

#print(f"Velocidad: {velocidadDeParpadeo}")