import socket

ipAddr = '127.0.0.1'
port = 1337

testMessage = 'Do you wanna build a snowman?'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ipAddr, port))
client_socket.send(testMessage.encode('b'))
received = client_socket.recv(1024)
print(received)
client_socket.close()