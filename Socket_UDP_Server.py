import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 1337))

while True:
        data, addr = server_socket.recvfrom(1024)
        print(data)