import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

primo_numero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (simbolo): ")
secondo_numero = float(input("Inserisci il secondo numero: "))
messaggio = {"primo_numero": primo_numero,
             "operazione": operazione,
             "secondo_numero": secondo_numero}
messaggio = json.dumps(messaggio)
s.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
s.close()