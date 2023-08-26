from socket import *

SERVER_PORT = 12345
SERVER_IP = 'localhost'

# Creating the client socket in order to make request to the server
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect to the server (Three-way-handshake)
client_socket.connect((SERVER_IP,SERVER_PORT))

