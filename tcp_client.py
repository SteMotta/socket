import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))
    sock_service.sendall(b'Hello, world!')
    data = sock_service.recv(DIM_BUFFER)

print('Received', data.decode())
sock_service.close()