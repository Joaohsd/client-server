from socket import *
import threading
import random
import json

from typing import List

from entity.question import Question
from db.questionDAO import QuestionDAO
from db.database import Database

def colored_text(text, color_code):
    return f"{color_code}{text}\033[0m"

def connection_handler(client_socket, client_address):
    # Using random to get which questions will be solved by the user
    sorted_questions = random.sample(range(1,11), 3)
    # Connect to the Database and get questions
    questions_json_str = getQuestionsFromDatabase(sorted_questions)
    # Send questions to the client
    answered_questions, questions_json = sendQuestions(client_socket, questions_json_str)
    # Send feedback to the client
    sendFeedback(client_socket, answered_questions, questions_json)
    # Close connection
    client_socket.close()
    
def sendQuestions(client_socket, questions_json_str):
    answered_questions = []
    questions_json = []
    # Iterate through questions sorted in other to send to the client
    for question in questions_json_str:
        client_socket.send(question.encode())
        answer = client_socket.recv(1024)
        answered_questions.append(int(answer.decode()))
        questions_json.append(json.loads(question))
    client_socket.send('FIM'.encode())
    return answered_questions, questions_json

def sendFeedback(client_socket, answered_questions, questions_json):
    # Iterate through questions sorted in other to send feedback to the client
    for index, question in enumerate(questions_json):
        if question['answer'] == answered_questions[index]:
            text = colored_text('Você acertou a questão ' + str(index+1) + '\n', "\033[32m")
        else:
            text = colored_text('Você errou a questão ' + str(index+1) + ' a resposta correta é ' + str(question['answer'] + 1) + '. ' + question['options'][question['answer']] + '\n', "\033[31m")
        client_socket.send(text.encode())
        client_socket.recv(1024)
    client_socket.send('FIM'.encode())

def getQuestionsFromDatabase(sorted_questions) -> List[Question]:
    db = QuestionDAO('C115-Trabalho1', 'Questions')
    questions = []
    for question_number in sorted_questions:
        question = db.readQuestion(id=question_number)
        questions.append(question)
        print('Question {question_number} got from DB')
    return questions

# Server IP and PORT for connections
SERVER_PORT = 12345
SERVER_IP = 'localhost'

# Reset database and create new one with the corresponding collection 'Questions'
db = Database('C115-Trabalho1', 'Questions')
db.resetDatabase()

# Create the server socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Start listening with a maximum of 10 clients in the queue
server_socket.listen(10)

print(f'Server listening on port {SERVER_PORT}')

while True:
    # Accepting connections
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from client {client_address}')
    # Create a thread to treat the connection established
    client_thread = threading.Thread(target=connection_handler, args=(client_socket, client_address))
    client_thread.start()

server_socket.close()