from socket import *
import json

SERVER_PORT = 12345
SERVER_IP = 'localhost'

# Creating the client socket in order to make request to the server
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect to the server (Three-way-handshake)
client_socket.connect((SERVER_IP,SERVER_PORT))

while True:
    question = client_socket.recv(1024).decode()
    if question == 'FIM':
        break
    question = json.loads(question)
    print(question['statement'])
    for index, option in enumerate(question['options']):
        print(str(index+1) + '. '+ option)
    answer = input('')
    client_socket.send(answer.encode())
    
while True:
    text = client_socket.recv(1024).decode()
    client_socket.send('OK'.encode())
    if text == 'FIM':
        break
    print(text)
