import socket
import threading

# The IP the server listens on
IP='0.0.0.0'

# The port the server listens on
PORT=9998


def main():
    # create server object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tell the server to start listening
    server.bind((IP,PORT))

    # Maximum of five incoming sessions are permitted to wait for the OS to 'accept'
    server.listen(5)
    
    # inform the user the server is now listening
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # receive the client socket in the client variable; 
        # store the remote connection details in the address variable
        client, address = server.accept()

        # display the source IP:PORT of the client connection
        print(f'[*]Accepted connection from {address[0]}:{address[1]}')

        # create a new thread object called 'client_handler'
        # when the threat actually starts, call the "handle_client" function and send the client socket to the handle_client function
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
    
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
