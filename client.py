import socket

name=input('Quel est votre pseudo?')

host, port = ('localhost', 5566)

try:

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.connect((host, port))

    print("Client connecté")

    data = name

    data = data.encode("utf8")

    socket.sendall(data)

    

    dataFromServer = socket.recv(1024)

    print(dataFromServer.decode());

    

except ConnectionRefusedError:

    print("connexion failed")

finally:
    socket.close()


    

