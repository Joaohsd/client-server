from socket import *
import threading
import random

from typing import List

from entity.question import Question
from db.questionDAO import QuestionDAO

def connection_handler(client_socket, client_address):
    # Using random to get which questions will be solved by the user
    sorted_questions = random.sample(range(1,11), 3)
    # Connect to the Database and get questions
    questions = getQuestionsFromDatabase(sorted_questions)
    for question in questions:
        print("Sending question to the Client")

def getQuestionsFromDatabase(sorted_questions) -> List[Question]:
    db = QuestionDAO('C115-Trabalho1', 'Questions')
    questions = []
    for question_number in sorted_questions:
        question = db.readQuestion(id=question_number)
        questions.append(question)
        print('Question {question_number} got from DB')
    return questions

SERVER_PORT = 12345
SERVER_IP = 'localhost'

# Create the server socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Start listening with a maximum of 5 clients in the queue
server_socket.listen(10)

print(f'Server listening on port {SERVER_PORT}')

while True:
    # Accepting connections
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from client {client_address}')

    # Create a thread to treat the connection established
    client_thread = threading.Thread(target=connection_handler, args=(client_socket, client_address))
    client_thread.start()
 