import socket

IP = "127.0.0.1"
PORT = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP, PORT))
    sock_server.listen() # Rimosso il buffer_size perché non serve nel listen, dove invece bisogna specificare il numero massimo di client collegati

    print(f"Server in ascolto su {IP}:{PORT}...")

    while True:
        sock_client, address_client = sock_server.accept()
        with sock_client:
            dati = sock_client.recv(DIM_BUFFER).decode()

            print(f"Ricevuto messaggio dal client {address_client}: {dati}")
            sock_client.sendall("Messaggio ricevuto dal server".encode())