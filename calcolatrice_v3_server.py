import socket
import json
from threading import Thread

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

def ricevi_comandi(socket_client, addr_client):
    print(f"Thread creato per il client {addr_client}")
    data = socket_client.recv(BUFFER_SIZE).decode()
    if not data:
        return
    print(f"Richiesta inviata dal client {addr_client}: {data}")
    data = json.loads(data)
    primo_numero = str(data["primo_numero"])
    operazione = data["operazione"]
    secondo_numero = str(data["secondo_numero"])
    risultato = eval(primo_numero + operazione + secondo_numero)
    socket_client.sendall(str(risultato).encode())
    socket_client.close()

def ricevi_connessioni(socket_listener):
    socket_client, addr_client = socket_listener.accept()
    try:
        Thread(target=ricevi_comandi, args=(socket_client, addr_client)).start()
    except Exception as e:
        print(f"Errore creazione thread: {e}")

def avvia_server(ip_server, port_server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        # Imposta l'opzione REUSEADDR per consentire la riutilizzazione dello stesso indirizzo dopo la chiusura del socket
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        socket_server.bind((SERVER_IP, SERVER_PORT))
        socket_server.listen(5) # Limite di 5 connessioni simultanee
        print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")
        while True:
            ricevi_connessioni(socket_server)

avvia_server(SERVER_IP, SERVER_PORT)