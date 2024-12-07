import socket

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")
    
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10000))
s.listen(3)
c, addr = s.accept()

msg = c.recv(2048).decode('utf-8')

with open('/tmp/aliensignallog.txt', 'w+') as afile:
  afile.write(msg)
for line in afile:
  print(line)