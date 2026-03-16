import socket
import json
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

print("Aspettando il calcolo da effettuare...")

while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    data = data.decode()
    print(f"Messaggio ricevuto dal client {addr}: {data}")
    if not data:
        break
    data = json.loads(data)
    primo_numero = data["primo_numero"]
    operazione = data["operazione"]
    secondo_numero = data["secondo_numero"]