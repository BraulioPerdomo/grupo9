import socket 
from time import sleep

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.219',999)
print('Iniciando servidor en {} puerto {}'.format(*server_address))

sock.bind(server_address)

sock.listen(1)

while True: 
    print("Esperando conexion")
    try:
        connecction, client_address = sock.accept()
        print ("Conexion aceptada desde", client_address)

        while True:
            data = connecction.recv(16)
            print('Dato recibido {!r}'.format(data))
            if(data):
                connecction.sendall (data)
                if (data == b'x'):
                    break
                else:
                    break
    finally:
        connecction.close()