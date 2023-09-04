from db.database import Database
from entity.question import Question
from service.questionService import QuestionService
import json

class QuestionDAO:
    def __init__(self, databaseName, collectionName):
        self.__db = Database(databaseName, collectionName)

    def createQuestion(self, question:Question) -> str:
        # Convert a question to JSON document
        questionDocument = QuestionService.setJsonDocumentByQuestion(question=question)
        
        try:
            result = self.__db.collection.insert_one(questionDocument)
            question_id = result.inserted_id
            print(f"Question {question.getId()} created with id: {question_id}")
        except Exception as error:
            print(f"An error occurred while creating question: {error}")
    
    def readQuestion(self, id:int):
        try:
            result = self.__db.collection.find_one({"_id": id})
            result = json.dumps(result)
            if result:
                print(f"Question found: {result}")

                return result
            else:
                print(f"No question found with id {id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading question: {error}")