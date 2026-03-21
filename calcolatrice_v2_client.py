import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

primo_numero = float(input("Inserisci il primo numero: "))
operazione = input("Inserisci l'operazione (simbolo): ")
secondo_numero = float(input("Inserisci il secondo numero: "))
messaggio = {"primo_numero": primo_numero,
             "operazione": operazione,
             "secondo_numero": secondo_numero}
messaggio = json.dumps(messaggio)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))
    sock_service.sendall(messaggio.encode("UTF-8"))
    data = sock_service.recv(BUFFER_SIZE)
    print(f"Risultato: {data.decode()}")