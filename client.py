import socket

def validate_ip(ip):
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

ip_adress=input("Entrez l'adresse IP du serveur : ")
while validate_ip(ip_adress) != True:
        ip_adress=input("Adresse IP non valide. ")

host, port = ('', 5566)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("Client connecté")

    data = "Client connecté"
    data = data.encode("utf8")
    socket.sendall(data)

    dataFromServer = socket.recv(1024)
    print(dataFromServer.decode());

except ConnectionRefusedError:
    print("Echec de connexion.")
finally:
    socket.close()


    

