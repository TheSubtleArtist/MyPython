#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send GET_KEY to download a string.
# The string is compressed with a common algorithm found in many
# websites. Uncompress the string and print it to get the flag.
#
import socket
import zlib
import gzip

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.send('GET_KEY'.encode())
data= s.recv(4096)
print(data)
gdata = gzip.decompress(data)
print(gdata)