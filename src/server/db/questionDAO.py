from db.database import Database
from entity.question import Question
from service.questionService import QuestionService

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
            if result:
                print(f"Question found: {result}")

                # Convert the JSON document to Question object
                question = QuestionService.setQuestionByJson(document=result)

                return question
            else:
                print(f"No question found with id {id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading question: {error}")