import socket

host, port = ('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("serveur démarré")

while True:
    socket.listen(5)
    conn, adress = socket.accept()
    print("en écoute")
    
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)
    
conn.close()
socket.close()
