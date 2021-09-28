import socket
import threading

class ThreadClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.conn = conn
		
	def run(self):
		data = conn.recv(1024)
		data = data.decode("utf8")
		print(data)
		
		conn.send("Hello Client!".encode('utf8'))

host, port = ('', 5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("serveur démarré")

while True:
    socket.listen(5)
    conn, adress = socket.accept()

    print("Accepted a connection request from %s:%s"%(conn, adress))
    
    my_thread = ThreadClient(conn)
    my_thread.start()
    
conn.close()
socket.close()