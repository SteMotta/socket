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
    if not data:
        break
    data = data.decode()
    print(f"Messaggio ricevuto dal client {addr}: {data}")
    data = json.loads(data)
    primo_numero = str(data["primo_numero"])
    operazione = data["operazione"]
    secondo_numero = str(data["secondo_numero"])
    risultato = eval(primo_numero + operazione + secondo_numero)
    print(f"Calcolo effettuato: {primo_numero} {operazione} {secondo_numero} = {risultato}")
    socket.sendto(str(risultato).encode(), addr)