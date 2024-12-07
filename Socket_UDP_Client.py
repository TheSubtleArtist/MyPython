import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"UDP is connectionless...\n", ("127.0.0.1", 1337))