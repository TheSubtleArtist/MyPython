import socket
import threading

addrIP = '0.0.0.0'
port = 9998

def handle_client(client_socket):
        with client_socket as sock:
                request = sock.recv(1024)
                print(f'[*] Received: {request.decode("utf-8")}')
                sock.send(b'ACK')
def main():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((addrIP, port))
        server_socket.listen(5)
        print(f'[*] Listening on {addrIP}:{port}')
        while True:
                client, address = server_socket.accept()
                print(f'[*] Accepted connection from {address[0]}:{address[1]}')
                client_handler = threading.Threat(target=handle_client, args=(client,))
                client_handler.start()

if __name__ == '__main__':
        main()
