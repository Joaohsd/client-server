from entity.question import Question
from typing import Dict

class QuestionService:
    @staticmethod
    def setQuestionByJson(document) -> Question:
        # Question information
        id = document["_id"]
        statement = document["statement"]
        options = document["options"]
        answer = document["answer"]

        # Create a question
        question = Question(id=id, statement=statement, options=options, answer=answer)

        return question

    @staticmethod
    def setJsonDocumentByQuestion(question:Question) -> Dict:
        # Cria um documento baseado no Animal
        documentoAnimal = {
            "_id": question.getId(),
            "statement": question.getStatement(),
            "options": question.getOptions(),
            "answer": question.getAnswer()
        }
       
        return documentoAnimal