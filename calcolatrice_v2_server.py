import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))
    sock_server.listen(BUFFER_SIZE)

    print(f"Server in ascolto su {SERVER_IP}:{SERVER_PORT}...")
    print("Aspettando il calcolo da effettuare...")
    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            data = sock_client.recv(BUFFER_SIZE).decode()
            if not data:
                break
            print(f"Messaggio ricevuto dal client {address_client}: {data}")
            data = json.loads(data)
            primo_numero = str(data["primo_numero"])
            operazione = data["operazione"]
            secondo_numero = str(data["secondo_numero"])
            print(f"Calcolo effettuato: {primo_numero} {operazione} {secondo_numero} = {eval(primo_numero + operazione + secondo_numero)}")