velocidadDeParpadeo = 1

f = open("configuracion.ini", "r")
lineas = f.readlines()

#print(lineas)
for linea in lineas:
    datos = linea.split('=')
    if (datos[0] == "velocidad"):
        velocidadDeParpadeo = int(datos[1])
    #print(datos)
f.close()

#print(f"Valocidad: {velocidadDeParpadeo}")