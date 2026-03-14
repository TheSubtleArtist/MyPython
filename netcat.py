# when servers don’t have netcat installed but do have Python
# This script is a Python implementation of basic netcat-style functionality.
# It can act as BOTH a client and server depending on command-line arguments.

import argparse        # For parsing command-line arguments
import socket          # For TCP networking
import shlex           # For safely splitting command strings into argument lists
import subprocess      # For executing system commands
import sys             # For system-level operations like stdin/stdout/exit
import textwrap        # For formatting help text nicely
import threading       # For handling multiple client connections simultaneously

# Main class implementing the netcat-like behavior
class NetCat:
    def __init__(self, args, buffer=None):
        # Store parsed CLI arguments
        self.args = args
        
        # Optional initial data buffer (used when piping data into the program)
        self.buffer = buffer
        
        # Create a TCP socket using IPv4
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Allow immediate reuse of the same IP/port after the program exits
        # (prevents "Address already in use" errors on restart)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Main execution selector
        # If --listen flag is set, run server mode
        # Otherwise run client mode
        def run(self):
                if self.args.listen:
                    self.listen()
                else:
                    self.send()
        
        # CLIENT MODE:
        # Connect to remote host and exchange data interactively
        def send(self):
            # Establish connection to target host/port
            self.socket.connect((self.args.target, self.args.port))
            
            # If we already have input data buffered, send it immediately
            if self.buffer:
                self.socket.send(self.buffer)

            try:
                # Loop forever handling incoming server responses and user input
                while True:
                    recv_len = 1
                    response = ''
                    
                    # Receive data until no more packets remain
                    while recv_len:
                        data = self.socket.recv(4096)   # read up to 4KB
                        recv_len = leng(data)           # length of received chunk
                        response += data.decode()       # convert bytes to string
                        
                        # If we received less than max buffer, assume transmission done
                        if recv_len < 4096:
                            break
                    
                    # If server sent something, print it
                    if response:
                        print(response)
                        
                        # Prompt user for next command/input
                        buffer == input('> ')
                        buffer += '\n'
                        
                        # Send user input back to server
                        self.socket.send(buffer.encode())
            
            # Allow user to exit with Ctrl+C
            except KeyboardInterrupt:
                print('User Terminated')
                self.socket.close()
                sys.exit
        
        # SERVER MODE:
        # Bind locally and wait for incoming connections
        def listen(self):
            
            # Bind to specified IP and port
            self.socket.bind((self.args.target, self.args.port))
            
            # Start listening with backlog queue size of 5 pending connections
            self.socket.listen(5)

            # Accept connections forever
            while True:
                client_socket, _ = self.socket.accept()
                
                # For each new client, create a separate thread
                # so multiple clients can be handled simultaneously
                client_thread = threading.Thread(
                    target=self.handle, args(client_socket,)
                )
                client_thread.start()
        
        # Function executed per-client connection
        def handle(self, client_socket):
            
            # OPTION 1: Execute a single command and return its output
            if self.args.execute:
                output = execute(self.args.execute)
                client_socket.send(output.encode())
            
            # OPTION 2: Receive uploaded file from client and save locally
            elif self.args.upload:
                file_buffer = b''
                
                # Receive file data in chunks
                while True:
                    data = client_socket.recv(4096)
                    if data:
                        file_buffer += data
                    else:
                        break
                
                # Write received bytes to disk
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer)
                
                # Notify client upload succeeded
                message = f'Saved file {self.args.upload}'
                client_socket.send(message.encode())
            
            # OPTION 3: Interactive command shell mode
            elif self.args.command:
                cmd_buffer = b''
                
                while True:
                    try:
                        # Send shell-style prompt to client
                        client_socket.send(b'BHP: #> ')
                        
                        # Keep receiving until newline entered
                        while '\n' not in cmd_buffer.decode():
                            cmd_buffer += client_socket.recv(64)
                        
                        # Execute received command locally
                        response = execute(cmd_buffer.decode())
                        
                        # Send command output back to client
                        if response:
                            client_socket.send(response.encode())
                        
                        # Reset command buffer for next input
                        cmd_buffer = b''
                    
                    # If anything goes wrong, shut down server
                    except Exception as e:
                        print(f'server killed{e}')
                        self.socket.close()
                        sys.exit()



# Helper function that executes OS commands safely
def execute(cmd):
    # Remove leading/trailing whitespace
    cmd=cmd.strip()
    
    # If empty command, do nothing
    if not cmd:
        return
    
    # Run the command and capture stdout + stderr
    output = subprocess.check_output(
        shlex.split(cmd),
        stderr=subprocess.STDOUT
    )
    
    # Return decoded string output
    return output.decode

# Entry point of script
if __name__ == '__main__':
    
    # Configure CLI parser
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        
        # Example usage shown in help text
        epilog=textwrap.dedent('''Example: 2
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        '''))
    
    # Command shell mode flag
    parser.add_argument('-c', '--command', action='store_true', help='command shell') 3
    
    # Execute specific command on connect
    parser.add_argument('-e', '--execute', help='execute specified command')
    
    # Listen mode (server)
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    
    # TCP port
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    
    # Target IP
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    
    # Upload destination filename
    parser.add_argument('-u', '--upload', help='upload file')
    
    # Parse arguments from command line
    args = parser.parse_args()
    
    # If listening, no stdin buffer needed
    if args.listen:
        buffer = ''
    else:
        # Otherwise read stdin for initial outgoing data
        buffer = sys.stdin.read()
    
    # Create NetCat instance
    nc = NetCat(args, buffer.encode())
    
    # Start execution (client or server)
    nc.run()