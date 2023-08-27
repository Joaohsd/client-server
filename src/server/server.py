from socket import *
import threading
import random
import json

from typing import List

from entity.question import Question
from db.questionDAO import QuestionDAO
from db.database import Database

def connection_handler(client_socket, client_address):
    # Using random to get which questions will be solved by the user
    sorted_questions = random.sample(range(1,11), 3)
    # Connect to the Database and get questions
    questions_json_str = getQuestionsFromDatabase(sorted_questions)
    answered_questions = []
    questions_json = []
    for question in questions_json_str:
        client_socket.send(question.encode())
        answer = client_socket.recv(1024)
        answered_questions.append(answer)
        questions_json.append(json.loads(question))

    client_socket.send('FIM'.encode())

    for index, question in enumerate(questions_json):
        if question['answer'] == answered_questions[index]:
            text = 'Você acertou a questão ' + str(index+1) + '\n'
            client_socket.send(text.encode())
            print(client_socket.recv(1024).decode())
        else:
            text = 'Você errou a questão ' + str(index+1) + ' a resposta correta é ' + str(question['answer'] + 1) + '. ' + question['options'][question['answer']] + '\n'
            client_socket.send(text.encode())
            print(client_socket.recv(1024).decode())
    
    client_socket.send('FIM'.encode())

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

# Reset database and create new one with the corresponding collection 'Questions'
db = Database('C115-Trabalho1', 'Questions')
db.resetDatabase()

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