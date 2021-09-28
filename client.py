import socket

ip_adress=input("Entrez l'adresse IP du serveur : ")

host, port = ('', 5566)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("Client connecté")

    data = "Client connecté"
    data = data.encode("utf8")
    socket.sendall(data)
    
except ConnectionRefusedError:
    print("Echec de connexion.")
finally:
    socket.close()
