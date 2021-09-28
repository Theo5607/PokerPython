import socket
import threading

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

class ThreadClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.conn = conn
		
	def run(self):
		data = conn.recv(1024)
		data = data.decode("utf8")
		print(data)
		
		conn.send("Vous êtes connecté au serveur", host+":"+str(port).encode('utf8'))

ip_adress=input("Entrez l'adresse IP locale du serveur : ")
while validate_ip(ip_adress) != True:
        ip_adress=input("Adresse IP non valide. ")

host, port = (ip_adress, 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur a démarré sur l'adresse", host+":"+str(port))

while True:
    socket.listen(5)
    conn, adress = socket.accept()

    print("Requête de connexion acceptée de la part de %s:%s"%(conn, adress))
    
    my_thread = ThreadClient(conn)
    my_thread.start()
    
conn.close()
socket.close()
