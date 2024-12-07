#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.send('GET_KEY'.encode())
key = s.recv(1024).decode()

key = key[::-1]

s.send(key.encode())

unkey = s.recv(1024).decode()

print(unkey)
       
       