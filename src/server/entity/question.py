from typing import List

class Question:
    def __init__(self, id:int, statement:str, options:list, answer:int):
        self.__id = id
        self.__statement = statement
        self.__options = options
        self.__answer = answer
    
    '''
        Getters
    '''
    def getId(self) -> int:
        return self.__id
    
    def getStatement(self) -> str:
        return self.__statement
    
    def getOptions(self) -> List[str]:
        return self.__options
    
    def getAnswer(self) -> int:
        return self.__answer
    
    '''
        Setters
    '''
    def setId(self, id):
        self.__id = id
    
    def setStatement(self, statement):
        self.__statement = statement
    
    def setOptions(self, options):
        self.__options = options
    
    def setAnswer(self, answer):
        self.__answer = answer
