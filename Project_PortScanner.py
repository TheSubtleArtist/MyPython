import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('clear', shell =True)

#Inputs
remoteServer = input('Enter remote host:')
lPort = int(input ('Enter the lowest port number to scan:'))
hPort = int(input ('Enter the highest port to scan:'))
remoteSErverIP = socket.gethostbyname(remoteServer)

#Banner of Information
print('-' * 60)
print(f'Please waith while scanning {remoteSErverIP}.')
print('-' * 60)

#Collect date and time of scan
tStart = datetime.now()

try:
    for port in range(lPort, hPort+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteSErverIP, port))
        if result == 0:
            print(f'Port {port}:  Open')
        sock.close()
except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print('Could not connect to server')
    sys.exit()

# Scan end time
tStop = datetime.now()

# total scan time
print(f'Scanning completed in: {tStop - tStart} seconds.')