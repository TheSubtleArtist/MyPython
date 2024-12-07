#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 10000))
s.send('ls /tmp'.encode())
print(s.recv(1024).decode())